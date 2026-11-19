# Q4 – Distance Vector (Bellman-Ford)

## Link Costs
A-B: 2, A-C: 7, B-C: 3, B-D: 8, C-D: 1, D-E: 4

## Round 1 Table (excerpt)
A to C: Direct = 7. But A -> B -> C = 2 + 3 = 5. **Cheaper!**

## Count to Infinity (Y-Z failure)
Y tells X it can reach Z (but it's via X).
X tells Y it can reach Z (but it's via Y).
Loop until INF (99).

## Poison Reverse
X tells Y: "My distance to Z is INF" (because X learned it from Y).
Y receives INF -> Y realizes link is dead. Loop broken.