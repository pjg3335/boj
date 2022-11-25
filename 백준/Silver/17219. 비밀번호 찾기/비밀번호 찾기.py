import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

mapper = {}
for _ in range(N):
    k, v = input().rstrip().split()
    mapper[k] = v

for _ in range(M):
    k = input().rstrip()
    print(mapper[k])