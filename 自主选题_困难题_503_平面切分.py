from math import gcd

n = int(input())
lines = set()
ans = 1
for _ in range(n):
    a, b = map(int, input().split())
    if (a, b) in lines:
        continue
    points = set()
    for c, d in lines:
        if a != c:
            x, y = d - b, a - c
            g = gcd(x, y)
            x, y = x // g, y // g
            if y < 0:
                x, y = -x, -y
            points.add((x, y))
    ans += len(points) + 1
    lines.add((a, b))
print(ans)
