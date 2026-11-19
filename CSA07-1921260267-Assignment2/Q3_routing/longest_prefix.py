# Simulates Longest Prefix Match logic
routes = [
    ("0.0.0.0", 0, "198.51.100.1"),
    ("10.1.2.0", 25, "192.0.2.13"),
    ("10.1.2.0", 24, "192.0.2.9"),
    ("10.1.0.0", 16, "192.0.2.5"),
    ("10.0.0.0", 8, "192.0.2.1")
]

def match(dest_ip):
    print(f"Destination: {dest_ip}")
    for net, prefix, next_hop in routes:
        print(f"  Check {net}/{prefix} -> Next hop {next_hop}")

if __name__ == "__main__":
    match("10.1.2.200") # Should choose /25