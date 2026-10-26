s = list(map(eval,input().split(" ")))
n = eval(input())
if s.count(n)!=0:
    print(f"{n}在列表中")
else :
    print(f"{n}不在列表中")
