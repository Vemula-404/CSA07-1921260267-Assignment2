def ospf_cost(link_mbps, ref_mbps=100):
    return max(1, int(ref_mbps / link_mbps))

links = [10, 100, 1000, 10000]
refs = [100, 100000] # Default vs 100 Gbps

for ref in refs:
    print(f"\nReference Bandwidth: {ref} Mbps")
    for l in links:
        print(f"  {l:5} Mbps -> Cost: {ospf_cost(l, ref)}")