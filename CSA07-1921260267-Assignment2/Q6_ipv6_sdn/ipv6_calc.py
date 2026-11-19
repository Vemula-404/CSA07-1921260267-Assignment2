import ipaddress

def compress_ipv6(addr):
    return str(ipaddress.IPv6Address(addr))

def eui64(mac):
    parts = mac.split(':')
    first_half = parts[:3]
    second_half = parts[3:]

    # Flip 7th bit
    first_byte = int(first_half[0], 16) ^ 0x02
    first_half[0] = f"{first_byte:02x}"

    eui = f"{''.join(first_half)}fffe{''.join(second_half)}"
    # Format for IPv6
    return f"fe80::{eui[0:4]}:{eui[4:8]}:{eui[8:12]}:{eui[12:16]}"

if __name__ == "__main__":
    addr = "2001:0db8:0000:0000:0000:ff00:0042:8329"
    print(f"Compressed: {compress_ipv6(addr)}")

    mac = "00:1A:2B:3C:4D:5E"
    print(f"EUI-64: {eui64(mac)}")