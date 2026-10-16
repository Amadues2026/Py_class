ans = 0
for n in range(4, 2021):
    if any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)):
        ans += 1
print(ans)
