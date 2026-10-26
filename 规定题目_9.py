import math

def Factorial(n):
    ans = sum(math.factorial(i) for i in range(1,n+1))
    return ans

n = int(input())
print(Factorial(n))
