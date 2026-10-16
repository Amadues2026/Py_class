s = input()
a = b = 0
for c in s:
    a, b = b, max(b, a + ord(c) - 96)
print(b)
