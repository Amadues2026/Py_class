cards = [2021] * 10
n = 1
while True:
    for c in str(n):
        cards[int(c)] -= 1
    if min(cards) < 0:
        break
    n += 1
print(n - 1)
