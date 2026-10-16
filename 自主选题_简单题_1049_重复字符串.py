from collections import Counter

k = int(input())
s = input()
if len(s) % k:
    print(-1)
else:
    length = len(s) // k
    print(sum(k - max(Counter(s[i::length]).values()) for i in range(length)))
