import sys

read = sys.stdin.readline
for _ in range(int(read())):
    n, m, k = map(int, read().split())
    l = r = k
    ans = 0
    while l <= n:
        ans += min(r, n) - l + 1
        l, r = (l - 1) * m + 2, r * m + 1
    print(ans)
