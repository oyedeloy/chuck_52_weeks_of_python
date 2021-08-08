#GETTING INFO FROM COMMAND OUTPUT
from pprint import pprint

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
print(show_interface_stats_lines) Each line becomes an element in a list
dele_2 = [item.strip() for item in show_interface_stats.splitlines()] Spaces were stripped after splitting each lines to become a list
print(dele_2)

for part_no, interface_info_part in enumerate(dele_2): Part_no will be the index no(Line number), interface_info_part will be each element in the list, dele_2 is the list.
    print(f"Info part {part_no}: {interface_info_part.strip()}")
    
"""

for index, Line in enumerate(show_interface_stats_lines):
    if Line.find("GigabitEthernet", 0) == 0:                   #for every line you look at, If you can find GigabitEthernet at location 0
        totals_line =  show_interface_stats_lines[index +5]    #go down five lines and we will deal with the element on the fifth line
                                                               #I will call that line the totals_line
                                                               #Everytime i see GigabitEthernet on a line, i will go to the totals_line
        interface_counters[Line] = totals_line.split()[1:]     # For every line with GigabitEthernet, it's totals_line will be split based on nothing
                                                               #If you split based on nothing, it defaults to blank
                                                               #Split it and take a slice of it, start from item 1 (index 2) and go all the way to the end
                                                               
print("\n\n-------- Interface Counters ----------------")
pprint(interface_counters)
  
      
  