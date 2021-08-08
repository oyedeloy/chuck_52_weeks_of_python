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
        subnet_address = ".".join(subnet_address_bytes)

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