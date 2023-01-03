import json
import time
import paho.mqtt.client as mqtt

REGISTER_DEVICE = "device/register"
DEVICE_REGISTER_MSG = "device/register_status"
DEVICE_STATUS = "device/status"
REGISTER_STATUS = "device/register/response/"

EdgeServer_HOST = "localhost"
EdgeServer_PORT = 1883
WAIT_TIME = 0.25


class Edge_Server:

    def __init__(self, instance_name):

        self._instance_id = instance_name
        self.client = mqtt.Client(self._instance_id)
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message
        self.client.connect(EdgeServer_HOST, EdgeServer_PORT, keepalive=60)
        self.client.loop_start()
        self._registered_device_list = []
        self._registered_room_list = []

    # Connect method to subscribe to various topics.     
    def _on_connect(self, client, userdata, flags, result_code):
        self.client.subscribe(REGISTER_DEVICE)
        self.client.subscribe(DEVICE_REGISTER_MSG)
        self.client.subscribe(DEVICE_STATUS)

        if result_code != 0:
            print("EdgeServer is Down {0} Result code of the error is :".format({str(result_code)}))
            if result_code == 4:
                print("MQTT broker is not running on the machine. Please start the MQTT broker on {0}, {1}".format(
                    EdgeServer_HOST, EdgeServer_PORT))

    # method to process the recieved messages and publish them on relevant topics 
    # this method can also be used to take the action based on received commands
    def _on_message(self, client, userdata, msg):

        if msg.topic == REGISTER_DEVICE:
            decode_msg = json.loads(msg.payload)
            print("\nRegistration request is acknowledged for device '{0}' in {1} ".format(decode_msg['device_id'],
                                                                                           decode_msg['room']))
            print("Request is processed for {0}.".format(decode_msg['device_id']))
            device_register_flag = True
            self._registered_device_list.append(decode_msg['device_id'])
            self._registered_room_list.append(decode_msg['room'])
            self.client.publish((REGISTER_STATUS + decode_msg['device_id']), json.dumps(device_register_flag), qos=2)
        elif msg.topic == DEVICE_REGISTER_MSG:
            decode_msg = json.loads(msg.payload)
            print("{0} - Registration status is available for '{1}' : {2}".format(decode_msg['msg'],
                                                                                  decode_msg['device_id'],
                                                                                  decode_msg['registered_status']))
        elif msg.topic == DEVICE_STATUS:
            decode_msg = json.loads(msg.payload)
            print("\nHere is the current device-status for {0}: {1}".format(decode_msg['device_id'], decode_msg))

    # Returning the current registered list
    def get_registered_device_list(self):
        return self._registered_device_list

    # Getting the status for the connected devices
    def get_status(self, cmd, cmd_type, cmd_group):
        if cmd_type == 'single':
            publish_topic = "device/"
            if cmd_group in self._registered_device_list:
                publish_topic += cmd_group
            self.client.publish(publish_topic, "get")

        # Publishing on the DEVICE_TYPE_TOPIC
        elif cmd_type == 'device_type':
            publish_topic = "device/" + cmd_group + "/"
            # if cmd_group == "light":
            #     publish_topic = "device/" + "light/"
            # elif cmd_group == "ac":
            #     publish_topic = "device/" + "ac/"
            self.client.publish(publish_topic, "get")

        # Publishing on the ROOM_TOPIC
        elif cmd_type == 'room':
            publish_topic = "device/" + cmd_group
            self.client.publish(publish_topic, "get")

        elif cmd_type == "all" and cmd_group == "all":
            for i in self._registered_device_list:
                publish_topic = "device/" + i
                self.client.publish(publish_topic, "get")

        return cmd

    # Controlling and performing the operations on the devices
    # based on the request received
    # Part of the problem statement 1.b.i, 2.a.iii, 2.b.iii. Complete this method to solve the problem
    def set_status(self, cmd, cmd_type, cmd_group, inputs):
        if cmd_type == 'single':
            publish_topic = "device/"
            if cmd_group in self._registered_device_list:
                publish_topic += cmd_group
            self.client.publish(publish_topic, inputs)

            # Publishing on the DEVICE_TYPE_TOPIC
        elif cmd_type == 'device_type':
            publish_topic = "device/" + cmd_group + "/"
            self.client.publish(publish_topic, inputs)

            # Publishing on the ROOM_TOPIC
        elif cmd_type == 'room':
            publish_topic = "device/" + cmd_group
            self.client.publish(publish_topic, inputs)

        elif cmd_type == "all" and cmd_group == "all":
            for i in self._registered_device_list:
                publish_topic = "device/" + i
                self.client.publish(publish_topic, inputs)
        return cmd

    def terminate(self):
        self.client.disconnect()
