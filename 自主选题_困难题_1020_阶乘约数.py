from collections import Counter

count = Counter()
for n in range(2, 101):
    p = 2
    while p * p <= n:
        while n % p == 0:
            count[p] += 1
            n //= p
        p += 1
    if n > 1:
        count[n] += 1
ans = 1
for e in count.values():
    ans *= e + 1
print(ans)
