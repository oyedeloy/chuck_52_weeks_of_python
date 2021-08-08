from pprint import pprint
from random import choice
import copy

from utility import create_network

device = {
    "name": "r3-L-n7",
    "vendor": "cisco",
    "model": "catalyst 2960",
    "os": "ios",
    "interfaces": [

    ]
}

print("\n\n----- device with no interfaces --------------------")
for key, value in device.items():
    print(f"{key:>16} : {value}")
interfaces = list() #The interfaces will be added to the dictionary above
for index in range (0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)
    
device["interfaces"] = interfaces
print("\n\n----- device with interfaces --------------------")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16} : {value}")
    else:
        print(f"{key:>16} :")
        for interface in interfaces:
            print(f"\t\t\t\t\t{interface}")
            
print()
print("\n\n----- device with interfaces using pprint--------------------")
pprint(device)

print("\n\n----- network with devices and interfaces --------------------")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)

print("\n----- information about network --------------------")
print(f"-- number of subnets: {len(network['subnets'])}")
print(f"-- list of subnets: {(network['subnets']).keys()}")
print(f"-- list of subnets w/o extraneous: {', '.join(network['subnets'])}")

print("\n----- network and devices nicely formatted --------------------")
for subnet_address, subnet in network["subnets"].items():
    print(f"\n-- subnet: {subnet_address}")
    for device in subnet["devices"]:
        print(f"   |-- device: {device['name']:8}  {device['ip']:10}  {device['vendor']:>10} : {device['os']}")


print("\n\n----- remember assignment vs shallow copy vs deep copy --------------------")
print("      modify 'network' only, and see if assign/copy/deepcopy versions reflect that change")

network_assign = network #The equal sign is not doing "copy" it sis an assignment operator.
                         #It assigns the vaiable name "network_assign" to network
                         #Both network and network_assign points to the same location in memory
                         #we are going to change a device name below and see the impact
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned"

print(f"  --- network == network_assign :    {network==network_assign}") #Returns a boolean
           #Any changes to network will also be applicable to the variable network_assign
        
#If you want a copy of "network" i.e, you don't want the copy to point to the same location in memory.

network_copy = copy.copy(network)

network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "another different name, copy this time"
print(f"  --- network == network_copy :      {network==network_copy}")
#You will be shocked that the result of the above code is True. They aare still the same
#This is because only the first level of data is copied.

#If you are going to copy everything such that you have your own copy and changes to one doesn't affect the other, use

network_deepcopy = copy.deepcopy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "this time with deep copy"
print(f"  --- network == network_deepcopy :  {network==network_deepcopy}")

                                                                         