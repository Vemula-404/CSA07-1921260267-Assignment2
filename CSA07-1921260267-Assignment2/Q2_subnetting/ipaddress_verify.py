import ipaddress

nets = ["192.168.10.0/25", "192.168.10.128/26", "192.168.10.192/27", "192.168.10.224/30"]
for net in nets:
    n = ipaddress.ip_network(net)
    print(f"{net:20s} hosts: {n.num_addresses - 2}")

# Test if Hostel (needs /26) fits
try:
    host = ipaddress.ip_network("192.168.10.228/26", strict=True)
    print(host)
except ValueError as e:
    print(f"Hostel cannot fit: {e}")