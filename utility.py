
from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

def create_devices(num_devices=1, num_subnets=1):
    created_devices = list()
    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return create_devices
    for subnet_index in range(1, num_subnets+1):
        for device_index in range(1, num_devices+1):
            device = dict()
    #GENERATE RANDOM DEVICE NAME
    # CHOOSE FROM THE LIST IN GENERATING A RANDOM NAME
            device["name"] = (
                choice(["R2", "R3", "R4", "R10"])
                + choice(["L", "U"])
                + choice(string.ascii_letters)
    ) 
    #CHOICE OF DEVICE VENDOR
            device["vendor"] = choice(["Cisco", "Juniper", "Arista"])
            if device["vendor"] == "Cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(["12.1(T).84", "14.7X", "8.12(S).010", "3.32(S).23"])
            elif device["vendor"] == "Juniper":
                device["os"] = "junos" 
                device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.83"])
            elif device["vendor"] == "Arista":
                device["os"] = "eos"
                device["version"] = choice(["2.43", "3.1.23", "3.67", "4.3.65"])
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)
    
    #ADD THE DEVICE TO  LIST OF DEVICES
            created_devices.append(device)
    return created_devices


def create_network(num_devices=1, num_subnets=1):

    # We'll re-use the create_devices function we created earlier,
    # then modify it to become an entire set of subnets, devices, and interfaces.

    devices = create_devices(num_devices, num_subnets)

    # Once again we are just going to consider the subnet to be the first three bytes
    # of the IP address, just to simplify things for teaching

    network = dict()
    network["subnets"] = dict()

    for device in devices:

        # There are many ways to get the subnet address from an IP address,
        # but for simplicity we are just going to replace the last byte with "0"
        subnet_address_bytes = device["ip"].split(".")
        subnet_address_bytes[3] = "0"
        subnet_address = ".".join(subnet_address_bytes)#Join subnet_address_bytes with dots

        if subnet_address not in network["subnets"]:

            network["subnets"][subnet_address] = dict()
            network["subnets"][subnet_address]["devices"] = list()

        network["subnets"][subnet_address]["devices"].append(device)

        # Add interfaces to the device we just processed
        interfaces = list()
        for index in range(0, choice([2, 4, 8])):
            interface = {
                "name": "g/0/0/" + str(index),
                "speed": choice(["10", "100", "1000"])
            }
            interfaces.append(interface)

        device["interfaces"] = interfaces

    return network
print("\n\n----- network with devices and interfaces --------------------")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)