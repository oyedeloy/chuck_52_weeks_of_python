
from tabulate import tabulate
from utility import create_devices

if __name__  == '__main__':

    devices = create_devices(num_devices=20, num_subnets=1)
    print("\n", tabulate(devices, headers="keys"))