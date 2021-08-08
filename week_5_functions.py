# SAME FUNCTIONALITY AS MULTIPLE DEVICE.PY USIND PYTHON FUCTIONS
from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

#THE CODE IN THE FUCTION IS THE SAME WITH MULTIPLE DEVICES.PY

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
                choice(["R2", "R3", "R4", "R6", "R10"])
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

if __name__  == '__main__':

    devices = create_devices(num_devices=20, num_subnets=1)
    print("\n", tabulate(devices, headers="keys"))
