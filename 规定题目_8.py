n = int(input())
ans = sum((2*i-1)/(2*i+1) for i in range(1,n+1) )
print(ans)
