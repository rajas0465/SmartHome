import json
import paho.mqtt.client as mqtt

# TOPICS USED TO SUBSCRIBE AND PUBLISH THE DATA

REGISTER_STATUS = "device/register/response/"
AC_DEVICES = "device/ac/"
REGISTER_DEVICE = "device/register"
DEVICE_REGISTER_MSG = "device/register_status"
DEVICE_STATUS = "device/status"

HOST = "localhost"
PORT = 1883


class AC_Device():
    _MIN_TEMP = 18
    _MAX_TEMP = 32

    def __init__(self, device_id, room):

        self._device_id = device_id
        self._room_type = room
        self._temperature = 22
        self._device_type = "AC"
        self._DEVICE_ID_TOPIC = "device/" + str(device_id)
        self._ROOM_TOPIC = "device/" + str(room)
        self._device_registration_flag = False
        self.client = mqtt.Client(self._device_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.on_disconnect = self._on_disconnect
        self.client.connect(HOST, PORT, keepalive=60)
        self.client.loop_start()
        self._register_device(self._device_id, self._room_type, self._device_type)
        self._switch_status = "OFF"

    # calling registration method to register the device
    def _register_device(self, device_id, room_type, device_type):
        while not self.client.is_connected():
            pass
        ac_device = dict()
        ac_device['device_id'] = device_id
        ac_device['room'] = room_type
        ac_device['type'] = device_type

        self.client.publish(REGISTER_DEVICE, json.dumps(ac_device))

    # Connect method to subscribe to various topics. 
    def _on_connect(self, client, userdata, flags, result_code):
        if result_code == 0:

            while not self.client.is_connected():
                pass
            self.client.subscribe(REGISTER_STATUS + self._device_id)
            self.client.subscribe(self._DEVICE_ID_TOPIC)
            self.client.subscribe(self._ROOM_TOPIC)
            self.client.subscribe(AC_DEVICES)
        else:
            print(
                "Bad connection for {0} instance {1} with result code : {2}".format(self._device_type, self._device_id,
                                                                                    str(result_code)))
            if result_code == 4:
                print("MQTT server is unavailable.")

    # on disconnect
    def _on_disconnect(self, client, userdata, flags, result_code):
        print("Disconnected with result code" + str(result_code))

    # method to process the recieved messages and publish them on relevant topics
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):
        received_message = (msg.payload.decode("utf-8")).split(',')
        # Publishing registartion status 

        if msg.topic == (REGISTER_STATUS + self._device_id):
            self._device_registration_flag = True
            ac_device_register = dict()
            ac_device_register['device_id'] = self._device_id
            ac_device_register['registered_status'] = self._device_registration_flag
            ac_device_register['msg'] = "AC-DEVICE Registered!"
            self.client.publish(DEVICE_REGISTER_MSG, json.dumps(ac_device_register))

        # Performing get or control operation based on the request received for direct device_id, device_type, or room_type      
        elif msg.topic in [self._DEVICE_ID_TOPIC, AC_DEVICES, self._ROOM_TOPIC]:
            if received_message[0] == 'get':
                # Status will be published at the end for set type message as well
                pass
            elif received_message[0] in ("ON", "OFF"):
                self._set_switch_status(received_message[0])
            elif type(received_message[0] == str):
                if self._switch_status != 'ON':
                    self._set_switch_status("ON")
                self._set_temperature(received_message[0])

                # Creating the payload to publish the status of the devices.
            ac_device_state = dict()
            ac_device_state['device_id'] = self._device_id
            ac_device_state['switch_state'] = self._get_switch_status()
            ac_device_state['temperature'] = self._get_temperature()
            self.client.publish(DEVICE_STATUS, json.dumps(ac_device_state))

    # Getting the current switch status of devices 
    # Part of the problem statement 1.a.iii. Complete this method to solve the problem
    def _get_switch_status(self):
        return self._switch_status

    # Setting the switch of devices
    # Part of the problem statement 1.b.iii. Complete this method to solve the problem
    def _set_switch_status(self, switch_state):
        self._switch_status = switch_state

    # Getting the temperature for the devices
    # Part of the problem statement 1.a.iii. Complete this method to solve the problem
    def _get_temperature(self):
        return self._temperature

        # Setting up the temperature of the devices

    # Part of the problem statement 2.a.iii. Complete this method to solve the problem
    def _set_temperature(self, temperature):
        if temperature in [str(i) for i in range(self._MIN_TEMP, self._MAX_TEMP + 1)]:
            self._temperature = temperature
        else:
            if temperature == "HIGH":
                self._temperature = 28
            elif temperature == "MEDIUM":
                self._temperature = 22
            elif temperature == "LOW":
                self._temperature = 18
            else:
                print("Temperature Change FAILED. Invalid temperature value received - " + temperature)
