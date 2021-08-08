from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint


devices = list()  # THIS CREATES AN EMPTY LIST TO STORE DEVICES

# WE WILL USE FOR LOOP TO CREATE LARGE NUMBER OF DEVICES

for index in range(10):
    # CREATE DEVICE DICTIONARY
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
    device["ip"] = "10.0.0." + str(index)
    #FORMATTED PRINT OF ONE DEVICE
    print()
    for key, value in device.items():
        print(f"{key:>16s} {value}")
    #ADD THE DEVICE TO  LIST OF DEVICES
    devices.append(device)
        
          
    
    

# WE WILL USE PPRINT TO PRINT DEVICES IN A RAW FORMAT
print("\n----- DEVICES AS A LIST OF DICTIONARY---------------")
pprint(devices)

# WE WILL PRINT A TABLE OF DEVICES USING THE TABULATE MODULE
print("\n----- SORTED DEVICES IN TABULAR FORMAT -------------")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
#print(tabulate(sorted(devices, key=itemgetter("vendor")), headers="keys"))