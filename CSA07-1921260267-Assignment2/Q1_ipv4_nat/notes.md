# Q1 – IPv4 Addressing & NAT

## Analysis Table
| Device | Address | Network | Broadcast | Valid? |
|---|---|---|---|---|
| Admission PC | 172.16.45.200/20 | 172.16.32.0 | 172.16.47.255 | Yes |
| Lab printer | 10.0.15.255/21 | 10.0.8.0 | 10.0.15.255 | **NO (Broadcast)** |
| X-ray server | 192.168.4.0/23 | 192.168.4.0 | 192.168.5.255 | **NO (Network)** |
| Clinic router | 203.0.113.10/29 | 203.0.113.8 | 203.0.113.15 | Yes |

## NAT Table (Source Port 50000)
- PC-A: 10.0.1.10:50000 -> 203.0.113.10:60001
- PC-B: 10.0.1.11:50000 -> 203.0.113.10:60002
*(Differentiated by outside port)*

## Datagram vs Virtual Circuit
Datagram routes independently (out-of-order possible, TCP fixes).
VC routes fixed path (in-order, but link failure breaks it).