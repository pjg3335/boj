from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

mx = 0

for c in combinations(cards, 3):
    sm = sum(c)
    if sm <= M:
        mx = max(mx, sm)

print(mx)