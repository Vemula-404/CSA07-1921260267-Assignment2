import ipaddress

def analyze(ip_str):
    iface = ipaddress.ip_interface(ip_str)
    net = iface.network
    print(f"Device: {ip_str}")
    print(f"  Network:   {net.network_address}")
    print(f"  Broadcast: {net.broadcast_address}")
    print(f"  Usable:    {net.network_address + 1} - {net.broadcast_address - 1}")
    print(f"  Valid Host? {'Yes' if iface.ip in net.hosts() else 'NO - Network/Broadcast'}")

if __name__ == "__main__":
    devices = ["172.16.45.200/20", "10.0.15.255/21", "192.168.4.0/23", "203.0.113.10/29"]
    for d in devices:
        analyze(d)