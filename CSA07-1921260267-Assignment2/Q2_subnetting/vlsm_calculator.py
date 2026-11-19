import math

def to_int(ip):
    a, b, c, d = map(int, ip.split("."))
    return a << 24 | b << 16 | c << 8 | d

def to_ip(n):
    return ".".join(str(n >> s & 255) for s in (24, 16, 8, 0))

def vlsm(base, needs):
    addr = to_int(base)
    print(f"{'Subnet':<10} {'Network':<18} {'Prefix':<6} {'Host Range':<30} {'Broadcast'}")
    for name, hosts in sorted(needs, key=lambda x: -x[1]):
        block = 1
        while block < hosts + 2:
            block *= 2
        prefix = 32 - int(math.log2(block))
        net = addr & (0xFFFFFFFF << (32 - prefix))
        bcast = net + block - 1
        print(f"{name:<10} {to_ip(net):<18} /{prefix:<5} {to_ip(net+1)+' - '+to_ip(bcast-1):<30} {to_ip(bcast)}")
        addr = bcast + 1
    print(f"\nNext free address: {to_ip(addr)}")

if __name__ == "__main__":
    vlsm("192.168.10.0", [("Labs", 100), ("Staff", 50), ("Library", 25), ("WAN", 2)])