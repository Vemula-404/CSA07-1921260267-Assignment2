# Q5 – OSPF (Link-State)

## Default Costs (Ref = 100 Mbps)
100 Mbps = 1
1 Gbps = 1
10 Gbps = 1
**Problem:** Cannot distinguish 1G from 10G.

## Fixed Costs (Ref = 100 Gbps)
1 Gbps = 100
10 Gbps = 10
**Result:** 10G path preferred.

## Dijkstra Result (R1)
- R4: 10 (Direct)
- R2: 100 (Direct)
- R3: 110 (via R2)
- R5: 20 (via R4)
- R6: 120 (via R4->R5 or R2->R3, tie)

## Multi-Area vs Single Area
Single area: < 50 routers.
Multi-area: ISP scale. Area 0 backbone. Summarization at ABRs.