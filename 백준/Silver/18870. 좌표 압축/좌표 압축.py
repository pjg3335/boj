import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))
rank = sorted(list(set(arr)))
mapper = {}
for i in range(len(rank)):
    mapper[rank[i]] = i

print(" ".join(map(lambda x: str(mapper[x]), arr)))