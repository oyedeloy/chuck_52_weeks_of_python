from pprint import pprint
device1_str = " r3-L-n7, cisco, catalyst 2968, ios "

#SPLIT

"""
You can split the string above based on anything you specify
For instance, the string above is splitted based on "comma"
When we use the split command on a string, the output is a list of strings.
"""
device1 = device1_str.split(",")
print("device1 using split")
print("    ", device1)

#STRIP
"""
Looking at the output, there are spaces before each
elements in the list. we can remove these spaces with the strip function
"""
device1 = device1_str.strip().split(",")
print("device1 using strip and split")
print("    ", device1)

"""However, the method above will only strip the space from the 
beginning and at the end of the original string (device1_str). The spaces
at the beginning of other elements were not removed
"""
#REMOVE ALL THE BLANKS
"""
You can replace all the blanks with nothing using the replace function
The problem with this is that the space between "catalyst" and "2960" will
also be replaced, making it less readable
"""
device1 = device1_str.replace(" ", "").split(",")
print("device1 using replace and split")
print("    ", device1)

#REPLACE BLANKS WITH COLON

"""
Replacing blanks with colon doesn't make it look good either as the output
is no longer a list of strings.
"""

device1 = device1_str.replace(" ", "").replace(",", ":").split(",")
print("device1 using replace(with colon) and split")
print("    ", device1)

#USING FOR LOOP TO STRIP

device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and split")
print("    ", device1)

#STRIP AND SPLIT USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print("    ", device1)



dele = "the quick brown fox jumps over the lazy dog"
wao = [item.strip() for item in dele.split(" ")]
print(wao)
 
#Finding a particular sub-string
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X86_64_IOSD-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
#we want to look for a particular value
expected_version = "Version 11.11.1a"
index = version.find(expected_version)
#print(index)
if index >=0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found: {expected_version}")

#Separating string component
print("\n\nSEPARATING VERSION STRING COMPONENT")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")

#ENUMERATION
print("\n\nSEPARATING VERSION STRING COMPONENT USING ENUMERATION")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part {part_no}: {version_info_part.strip()}")

#GETTING INFO FROM COMMAND OUTPUT

show_interface_stats = """
GigabitEthernet1
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor      25376    1529598       8242     494554
             Route cache          0          0          0          0
       Distributed cache     496298   60647894     673003  218461079
                   Total     521674   62177492     681245  218955633
GigabitEthernet2
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor         19       1140          0          0
             Route cache          0          0          0          0
       Distributed cache       6077     663304          0          0
                   Total       6096     664444          0          0
Interface GigabitEthernet3 is disabled
Loopback21
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          0          0
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          0          0
Loopback55
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0          3        241
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0          3        241
Loopback100
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor          0          0         43       2806
             Route cache          0          0          0          0
       Distributed cache          0          0          0          0
                   Total          0          0         43       2806
"""


#SPLITLINES
"""
When you have multi-line output, the "splitline" method is very handy.
Each line in the output will become a string, meaning, each line will become 
an element in a list.
"""
interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()

"""
print(show_interface_stats_lines)
dele_2 = [item.strip() for item in show_interface_stats.splitlines()]
print(dele_2)

for part_no, interface_info_part in enumerate(dele_2):
    print(f"Info part {part_no}: {interface_info_part.strip()}")
"""
