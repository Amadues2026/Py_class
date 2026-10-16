n = int(input())
ans = int(str(abs(n))[::-1])
print(-ans if n < 0 else ans)
