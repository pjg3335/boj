import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
vectors = ((0,1),(0,-1),(1,0),(-1,0))


def validate(x, y):
    return 0<=x<M and 0<=y<N and arr[y][x] == 0

def bfs():
    q = deque()
    max_d = 0
    unripe_cnt = 0

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1: q.append((x,y,0))
            if arr[y][x] == 0: unripe_cnt += 1
    
    while q:
        x, y, d = q.popleft()
        max_d = max(d, max_d)

        for vx, vy in vectors:
            nx, ny = (x+vx, y+vy)
            if validate(nx, ny):
                unripe_cnt -= 1
                arr[ny][nx] = 1
                q.append((nx, ny, d+1))

    return max_d if unripe_cnt == 0 else -1

print(bfs())