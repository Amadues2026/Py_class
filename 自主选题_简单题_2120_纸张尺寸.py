n = int(input()[1:])
a, b = 1189, 841
for _ in range(n):
    a, b = b, a // 2
print(a)
print(b)
