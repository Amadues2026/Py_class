n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=sum)
time = ans = 0
for s, t, e in a:
    ans += time + s + t
    time += s + t + e
print(ans)
