s = list(map(eval, input().split()))
for i in range(len(s) - 1):
    k = i
    for j in range(i + 1, len(s)):
        if s[j] < s[k]:
            k = j
    s[i], s[k] = s[k], s[i]
    print(s)
print(s)
