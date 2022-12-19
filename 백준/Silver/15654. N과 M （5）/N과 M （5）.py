from itertools import permutations

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in permutations(arr, M):
    print(" ".join(list(map(str, i))))