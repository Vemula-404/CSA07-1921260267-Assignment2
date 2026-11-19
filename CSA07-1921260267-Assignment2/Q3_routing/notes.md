# Q3 – Longest Prefix Match & Static Routing

## LPM Results
- 10.1.2.200 -> /25 via 192.0.2.13 (most specific)
- 10.1.2.10  -> /24 via 192.0.2.9
- 10.2.0.1   -> /8 via 192.0.2.1
- 192.0.2.55 -> /0 (default) via 198.51.100.1

## Config
- Serial needs `clock rate 64000` on DCE side.
- Floating static route: `ip route ... 200` (higher AD = backup).

## OSPF vs Static
2 campuses: Static is simpler.
5 campuses: OSPF is better (auto-recovery, less manual config).