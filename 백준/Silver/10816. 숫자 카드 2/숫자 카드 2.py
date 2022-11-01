from collections import defaultdict

N = int(input())
cards = defaultdict(int)
for n in map(int, input().split()): cards[n] += 1

M = int(input())
print(" ".join(list(map(lambda n:str(cards[n]), map(int, input().split())))))