from math import gcd
from heapq import heappush, heappop

d = [float('inf')] * 2022
d[1] = 0
q = [(0, 1)]
while q:
    distance, u = heappop(q)
    if distance != d[u]:
        continue
    for v in range(max(1, u - 21), min(2021, u + 21) + 1):
        value = distance + u * v // gcd(u, v)
        if value < d[v]:
            d[v] = value
            heappush(q, (value, v))
print(d[2021])
