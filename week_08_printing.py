from pprint import pprint
from operator import itemgetter
from tabulate import tabulate
from datetime import datetime
from time import sleep
from random import choice
import nmap
from utility import create_devices



devices = create_devices(25)
#USING PRINT
print("\n\n----------USING PRINT----------\n")
print(devices)

#USING PPRINT
print("\n\n----------USING PPRINT----------\n")
pprint(devices)

#USING LOOP
print("\n\n----------USING LOOP----------\n")
for device in devices:
    sleep(0.1)
    device["last_heard"] = str(datetime.now())  #Create the last heard key in the dictionary
                                                #Then set the value to now. 
    print(devices)


#USING TABULATE
print("\n\n----------USING TABULATE----------\n")
print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))


#USING LOOP AND FSTRING (manual tabulation)
print("\n\n----------USING LOOP AND FSTRING----------\n")
print("   NAME      VENDOR : OS      IP ADDRESS       LAST HEARD")
print("  -----     -------   -----   --------------   ----------------------")


for device in devices:
    print(f'{device["name"]:>7} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:<15} {device["last_heard"][:-4]}')
    #device["last_heard"][:-4]} = use the "last heard string minus the last four Xracter" (index slicing)
    
    
    
#USING LOOP AND FSTRING (sort descending by "last_heard")
print("\n\n----------SAME AS ABOVE WITH SORT DECSENDING----------\n")
for device in sorted(devices, key=itemgetter("last_heard"), reverse=True):
    print(f'{device["name"]:>7} {device["vendor"]:>10} {device["os"]:<6} {device["ip"]:<15} {device["last_heard"][:-4]}')
    
    
#MULTIPLE PRINT STATEMENT ON THE SAME LINE    
print("\n\nMULTIPLE PRINT STATEMENTS, SAME LINE")
print("Testing Devices:")  
for device in devices:
    print(f"--- testing device {device['name']} ... ", end="")
    sleep(choice([0.1, 0.2, 0.3, 0.4]))
    print("done.")
print("Testing completed") 

nm = nmap.PortScanner()
while True:
    ip = input("\nInput IP address to scan: ")
    if not ip:
        break
    print(f"\n--- beginning sacn of {ip}") 
    output = nm.scan(ip, "22-1024")
    print("----- nmap scan output--------------")
    print(output)

