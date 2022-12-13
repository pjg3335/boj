from itertools import combinations

N, M = map(int, input().rstrip().split())
for c in combinations(range(1, N+1), M):
    print(" ".join(list(map(str ,c))))