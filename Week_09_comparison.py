from utility import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime



devices = create_devices(num_subnets=2, num_devices=25)

#USING LOOP AND FSTRING (manual tabulation)
print("\n   NAME      VENDOR : OS      IP ADDRESS       VERSION")
print("  -----     -------   -----   --------------   -----------")
for device in devices:
    print(f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}   {device["version"]}')


print("\n   NAME      VENDOR : OS      IP ADDRESS       VERSION")
print("  -----     -------   -----   --------------   -----------")
for device in devices:
    if device["vendor"].lower() == "cisco":
        print(f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}   {device["version"]}')

print("\n----- Starting comparison of device names --------------------")
for index, device_a in enumerate(devices): #We are interested in both the device and the index 
    for device_b in devices[index+1:]: #this second loop starts from where we are currently and adds one to it i.e the nex device
                                       #That means you are comparing the current index to the rest of the indexes.
        if device_a["name"] == device_b["name"]:
            print(f"found match! {device_a['name']} for both {device_a['ip']} and {device_b['ip']}")
            
            print("----- Comparison of device names completed")
            
            
print("\n----- Create table of arbitrary 'standard' versions for each vendor:os --------------------")
standard_versions = dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    #print(vendor_os)
    if vendor_os not in standard_versions: #comparing each vendor os to the dict
        standard_versions[vendor_os] = device["version"] #if vendor os doesn't exist in the dict, create it
                                                         #It will make the first version it sees the arbitrary version number

pprint(standard_versions)

#Comparing every created device version to the arbitrary standard version
print("\n----- Create list of non-compliant device OS versions for each vendor:os --------------------")
non_compliant_devices = dict() #Creates a dictionary of non-compliant devices
for vendor_os, _ in standard_versions.items(): #An _ can mean a lot in python depending on where you are using it
                                               #In this case, it means we are only looking at the keys and not interested in the values
                                               #.keys can be used to achieve the same objective.
    
    
    non_compliant_devices[vendor_os] = [] #Creating a list of devices that don't comply with the standard version

for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if device["version"] != standard_versions[vendor_os]: #standard version[vendor_os] returns the value of a dict item
        non_compliant_devices[vendor_os].append(device["ip"] + "  version: " + device["version"])
pprint(non_compliant_devices)

#Assignment, copy, and deep copy
       
print("\n\n----- Assignment, copy, and deep copy --------------------")
devices2 = devices #Devices2 will always point at devices. It is not a brand new copy.
devices[0]["name"] =="This name is dumb" #The first dictionary item, and the key "name", was set to
                                         #"this name is dumb"
if devices2 == devices:
    print("\n    Assignment and modification: devices2 STILL equals devices")
    print("    ---> Moral: Assignment is NOT the same as copy!")
else:
    print("    Huh?")
    
from copy import copy
from copy import deepcopy

devices2 = copy(devices) #is this a brand new copy? NO!!
                         #This is a shallow copy and it copies the first layer of stuffs 
devices2[0]["name"] =="This name is also dumb" #Here, we have gone beyond the first layer to change stuff
                                               #Therefore, devices2 and devices will still be the same
if devices2 == devices:
    print("\n    Shallow copy and modification: devices2 STILL equals devices")
    print("    ---> Moral: 'copy()' only does a SHALLOW (1st level) copy!")
    print("    ---> Result: Uh-oh - I just screwed up the original version!!")
else:
    print("    Huh?")
    
devices2 = deepcopy(devices)
devices2[0]["name"] = "this is ANOTHER dumb device name"
if devices2 == devices:
    print("    Huh?")
else:
    print("\n    Deep copy and modification: devices2 no longer equals devices")
    print("    ---> Moral: 'deepcopy()' gives you a complete copy of the original!")
    print("    ---> Result: I can do whatever I want with my copy, without touching the original!!")
    
    
#Create new set of devices
new_set_of_devices = create_devices(num_subnets=2, num_devices=25)
if new_set_of_devices == devices:
    print("    Huh?")
else:
    print("\n    Comparisons of complex, deep data is easy in Python")
    print("    ---> Moral: you can compare any two data structures, no matter how deeply nested")
    
    
print("\n\n----- Comparisons for implementing SLAs --------------------\n")
SLA_AVAILABILITY = 96
SLA_RESPONSE_TIME = 1.0
devices = create_devices(num_subnets=2, num_devices=25)
for device in devices:
    device["availability"] = randint(94, 100) #Assign a randon integer btwn 94 and 100
    device["response_time"] = uniform(0.5, 1.1) #Asign randomly between 0.5 and 1.1
    if device["availability"] < SLA_AVAILABILITY:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_AVAILABILITY}"  )
    if device["response_time"] > SLA_RESPONSE_TIME:
        print(f"{datetime.now()}: {device['name']:6} - Response Time {device['response_time']:.3f} > {SLA_RESPONSE_TIME}")
        
        
print("\n\n----- Comparing classes --------------------")


class DeviceWithEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip

    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq):
            return False
        return self.name == other.name and self.ip_address == other.ip_address



    
    
    
                                        
