import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [0]+list(map(int, input().rstrip().split()))
for i in range(1, len(arr)): arr[i] = arr[i-1]+arr[i]

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    print(arr[e]-arr[s-1])