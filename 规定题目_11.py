def single(n):
    ans = []
    for x in n:
        if x not in ans:
            ans.append(x)
    return ans

s = list(input())
print(single(s))
