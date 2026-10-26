n = int(input())
dp = [int(input())]
for i in range(1, n):
    a = list(map(int, input().split()))
    dp = [a[j] + max(dp[j - 1] if j > 0 else -1, dp[j] if j < i else -1) for j in range(i + 1)]
print(max(dp[(n - 1) // 2:n // 2 + 1]))
