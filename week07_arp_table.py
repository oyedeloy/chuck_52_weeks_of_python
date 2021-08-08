from pprint import pprint
"""
This program takes the output of the show arp command and turns it into
a table of ip address and the corresponding mac address that goesn with it.
"""

show_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.10.20.48             -   0050.56bb.e99c  ARPA   GigabitEthernet1
Internet  10.10.20.200           14   0050.56bb.8be2  ARPA   GigabitEthernet1
Internet  10.10.20.254            0   0896.ad9e.444c  ARPA   GigabitEthernet1

"""

arp_table = dict()                                 #Crate an empty dictionary to hold the values
for Line in show_arp.splitlines():
    if Line.lower().find("internet", 0) == 0:           #For every line in show_arp, if you find internet at location 0
        arp_table[Line[10:25].strip()] = Line[38:52]   #The arp_table dictionary will have a key of slice [10:25] and a value of slice [38:52]
print("\n\n-------ARP Table ---------------")
pprint(arp_table)
    