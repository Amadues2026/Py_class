s = input()
i = ans = 0
while i + 1 < len(s):
    if s[i] == s[i + 1] or s[i] == '?' or s[i + 1] == '?':
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
