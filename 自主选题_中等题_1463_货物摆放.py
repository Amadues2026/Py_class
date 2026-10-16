n = 2021041820210418
p = 2
ans = 1
while p * p <= n:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    ans *= (e + 1) * (e + 2) // 2
    p += 1
if n > 1:
    ans *= 3
print(ans)
