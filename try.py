ip = "10.0.3.4"
subnet_address_bytes = ip.split(".")
print(subnet_address_bytes)
subnet_address_bytes[3] = "0"
print(subnet_address_bytes)
subnet_address = ".".join(subnet_address_bytes)
print(subnet_address)

