# Q2 – Subnetting (VLSM)

## VLSM Plan (Largest First)
| Subnet | Network | Prefix | Range |
|---|---|---|---|
| Labs | 192.168.10.0 | /25 | .1 - .126 |
| Staff | 192.168.10.128 | /26 | .129 - .190 |
| Library | 192.168.10.192 | /27 | .193 - .222 |
| WAN | 192.168.10.224 | /30 | .225 - .226 |

## Hostel Trap
60 hosts need /26 (62 usable).
Free space: 192.168.10.228 to .255 (28 addresses).
**28 < 64** → Cannot fit. Requires new subnet (e.g., 192.168.11.0/26).

## Route Summarisation
172.16.8.0/24 to 172.16.11.0/24 -> **172.16.8.0/21** (Common prefix 00001xxx).