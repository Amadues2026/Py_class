n = int(input())
a = [int(input()) for _ in range(n)]
for score in (60, 85):
    count = sum(x >= score for x in a)
    print(str((200 * count + n) // (2 * n)) + '%')
