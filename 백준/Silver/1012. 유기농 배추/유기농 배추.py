import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())
vectors = ((1,0),(-1,0),(0,1),(0,-1))

def dfs(x, y):
    arr[y][x] = 0
    for vx, vy in vectors:
        nx, ny = (x+vx, y+vy)
        if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 1:
            dfs(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    
    ans = 0
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                dfs(x, y)
                ans += 1
    print(ans)