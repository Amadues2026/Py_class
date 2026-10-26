import sys

read = sys.stdin.readline
n = int(read())
parent = [0] * (n + 1)
count = [0] * (n + 1)
height = [0] * (n + 1)
for i in range(2, n + 1):
    parent[i] = int(read())
    count[parent[i]] += 1
for i in range(n, 1, -1):
    height[i] += count[i]
    p = parent[i]
    height[p] = max(height[p], height[i])
print(height[1] + count[1])
