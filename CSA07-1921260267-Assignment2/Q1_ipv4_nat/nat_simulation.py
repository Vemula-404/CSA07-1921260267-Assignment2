# Simulates the clinic router's NAT translation table
nat_table = {}

def translate_out(src_ip, src_port, dst_ip, dst_port):
    outside_port = 60000 + len(nat_table) + 1
    nat_table[(outside_port, dst_ip, dst_port)] = (src_ip, src_port)
    print(f"Inside {src_ip}:{src_port} -> Outside 203.0.113.10:{outside_port} -> {dst_ip}:{dst_port}")

def translate_in(dst_port, src_ip, src_port):
    if (dst_port, src_ip, src_port) in nat_table:
        real_ip, real_port = nat_table[(dst_port, src_ip, src_port)]
        print(f"Outside :{dst_port} -> Translated back to {real_ip}:{real_port}")

if __name__ == "__main__":
    translate_out("10.0.1.10", 50000, "198.51.100.50", 443)
    translate_out("10.0.1.11", 50000, "198.51.100.50", 443)