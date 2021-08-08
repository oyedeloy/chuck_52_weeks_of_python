
from pprint import pprint


device = {
    "name": "S1",
    "vendor": "Cisco",
    "model": "CSR_1000V",
    "os": "NXOS",
    "Version":"15.2",
    "ip": "192.168.1.1",
}


# REGULAR PRINTS
print("\n____ REGULAR PRINT _____")
print("device", device)
print("device name", device["name"])

#PRETTY PRINT
print("\n_____PRETTY PRINT_______")
pprint(device)

# FORMATTED PRINT
print('\n_____FORMATTED USING F-STRINGS AND FOR LOOPS_____')
for key, value in device.items():
    #give me 16 characters of space and right justify it(Use 16 Xracters to print it out)
    #The right justification make the columns allign
    print(f"{key:>16s} :{value}")