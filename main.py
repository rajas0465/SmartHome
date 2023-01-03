import time
from EdgeServer import Edge_Server
from LightDevice import Light_Device
from ACDevice import AC_Device

WAIT_TIME = 0.25  

print("\nSmart Home Simulation started.")

edge_server_1 = Edge_Server('edge_server_1')
time.sleep(WAIT_TIME)  

print("\n******************* REGSITRATION OF THE DEVICES THROUGH SERVER *******************")

print("\n******************* REGSITRATION OF LIGHT DEVICES INITIATED *******************")

light_device_1 = Light_Device("light_1", "Kitchen")
time.sleep(WAIT_TIME)  
light_device_2 = Light_Device("light_2", "Garage")
time.sleep(WAIT_TIME)  
light_device_3 = Light_Device("light_3", "BR1")
time.sleep(WAIT_TIME)  
light_device_4 = Light_Device("light_4", "BR2")
time.sleep(WAIT_TIME)  
light_device_5 = Light_Device("light_5", "Living")
time.sleep(WAIT_TIME)  

print("\n******************* REGSITRATION OF AC DEVICES INITIATED *******************")

ac_device_1 = AC_Device("ac_1", "BR1")
time.sleep(WAIT_TIME)  
ac_device_2 = AC_Device("ac_2", "Living")
time.sleep(WAIT_TIME)  
ac_device_3 = AC_Device("ac_3", "Living")
time.sleep(WAIT_TIME)  

print("\n******************* REGSITRED DEVICES ON THE SERVER *******************")

print("\nFetching the list of registered devices from EdgeServer")
registered_devices = edge_server_1.get_registered_device_list()
print("The Registered devices on Edge-Server:")
print(registered_devices)

# GETTING STATUS OPERATIONS FOR ALL THE TEST CASES

print("\n******************* GETTING THE STATUS AND CONTROLLING THE DEVICES *******************")

print("\n******************* GETTING THE STATUS BY DEVICE_ID *******************")

cmd = 1
print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'light_1')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'light_2')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'light_3')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'light_4')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'light_5')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'ac_1')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'ac_2')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on device_id: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'single', 'ac_3')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\n******************* GETTING THE STATUS BY DEVICE_TYPE *******************")


print("\nStatus based on: LIGHT DEVICE TYPE ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'device_type', 'light')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nStatus based on: AC DEVICE TYPE")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'device_type', 'ac')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\n******************* GETTING THE STATUS BY ROOM_TYPE *******************")


print("\nStatus based on room: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'room', 'Living')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\n******************* GETTING THE STATUS BY ENTIRE_HOME *******************")


print("\nStatus based on room: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'all', 'all')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

# SETTING OPERATIONS FOR ALL THE TEST CASES

print("\n******************* SETTING UP THE STATUS AND CONTROLLING THE DEVICE_ID *******************")

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'single', 'light_1', 'ON')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'single', 'ac_1', 'ON')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'single', 'light_1', 'MEDIUM')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1


print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'single', 'ac_1', 29)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'single', 'light_2', 'HIGH')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1


print("\n******************* SETTING UP THE STATUS AND CONTROLLING BY THE DEVICE_TYPE *******************")

print("\nControlling the devices based on TYPE: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'device_type', 'ac', 21)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on TYPE: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.set_status(cmd, 'device_type', 'light', 'MEDIUM')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\n******************* SETTING UP THE STATUS AND CONTROLLING BY ROOM *******************")


print("\nControlling the devices based on room: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'room', 'Living', 30)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on room: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'all', 'all', 28)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1


print("succeded")

print("\nControlling the devices based on room: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'room', 'Living', 'HIGH')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\n******************* SETTING UP THE STATUS AND CONTROLLING FOR INVALID REQUESTS *******************")

print("\nControlling the devices based on room: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'all', 'all', 38)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'single', 'ac_1', 39)
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1

print("\nControlling the devices based on ID: ")
print("\nCommand ID " + str(cmd) + " request is initiated.")
status = edge_server_1.set_status(cmd, 'single', 'light_4', 'HIGH')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1


print("\n******************* CURRENT STATUS BEFORE CLOSING THE PROGRAM *******************")

print("\nStatus based on room: ")
print("\nCommand ID " + str(cmd) + " request is intiated.")
status = edge_server_1.get_status(cmd, 'all', 'all')
time.sleep(WAIT_TIME)  
print("\nCommand ID " + str(status) + " is executed.")
cmd += 1


print("\nSmart Home Simulation stopped.")
edge_server_1.terminate()
