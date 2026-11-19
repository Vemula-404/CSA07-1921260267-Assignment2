INF = 99
names = "ABCDE"
cost = {("A","B"):2, ("A","C"):7, ("B","C"):3, ("B","D"):8, ("C","D"):1, ("D","E"):4}

link = {}
for (u, v), c in cost.items():
    link[u, v] = link[v, u] = c

# Initialize table
table = {u: {v: (0 if u == v else link.get((u, v), INF)) for v in names} for u in names}

rounds = 0
changed = True
while changed:
    changed = False
    rounds += 1
    old = {u: dict(table[u]) for u in names}
    for u in names:
        for n in names:
            if (u, n) not in link:
                continue
            for dest in names:
                via_n = link[u, n] + old[n][dest]
                if via_n < table[u][dest]:
                    table[u][dest] = via_n
                    changed = True

print(f"Converged after {rounds} rounds")
for u in names:
    print(u, " ".join(f"{table[u][v]:2d}" for v in names))

# Simulate Count-to-Infinity (Y-Z fails)
print("\nSimulating Y-Z failure (X-Y-Z topology)...")
X, Y, Z = 'X', 'Y', 'Z'
# Implementation of the loop count...