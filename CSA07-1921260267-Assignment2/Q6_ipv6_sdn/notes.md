# Q6 – IPv6, ICMP, Multicast, SDN

## IPv6 Compression
Full: 2001:0db8:0000:0000:0000:ff00:0042:8329
Compressed: 2001:db8::ff00:42:8329

## EUI-64
MAC: 00:1A:2B:3C:4D:5E
1. Insert FFFE: 00:1A:2B:FF:FE:3C:4D:5E
2. Flip 7th bit (00 -> 02)
Result: 021A:2BFF:FE3C:4D5E
Link-local: fe80::021a:2bff:fe3c:4d5e