s = input()
a = min(set(s), key=lambda x: (-s.count(x), x))
print(a)
print(s.count(a))
