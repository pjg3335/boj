from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

H, V, D = (0,1,2)
# dp[y][x][모양]
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1,0,0]
for x in range(2, N):
    if arr[0][x] == 1: break
    dp[0][x][H] = dp[0][x-1][H]

for x in range(2, N):
    for y in range(1, N):
        if arr[y][x] == 1: continue
        if arr[y][x-1] != 1:
            dp[y][x][H] = (dp[y][x-1][D]+dp[y][x-1][H])
        if arr[y-1][x] != 1:
            dp[y][x][V] = (dp[y-1][x][D]+dp[y-1][x][V])
        if arr[y][x-1] != 1 and arr[y-1][x] != 1 and arr[y-1][x-1] != 1:
            dp[y][x][D] = (dp[y-1][x-1][D]+dp[y-1][x-1][V]+dp[y-1][x-1][H])

print(sum(dp[N-1][N-1]))