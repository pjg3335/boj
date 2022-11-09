import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
vectors = ((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))


def validate(x, y, z):
    return 0<=x<M and 0<=y<N and 0<=z<H and arr[z][y][x] == 0

def bfs():
    q = deque()
    max_d = 0
    unripe_cnt = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if arr[z][y][x] == 1: q.append((x,y,z,0))
                if arr[z][y][x] == 0: unripe_cnt += 1
    
    while q:
        x, y, z, d = q.popleft()
        max_d = max(d, max_d)

        for vx, vy, vz in vectors:
            nx, ny, nz = (x+vx, y+vy, z+vz)
            if validate(nx, ny, nz):
                unripe_cnt -= 1
                arr[nz][ny][nx] = 1
                q.append((nx, ny, nz, d+1))

    return max_d if unripe_cnt == 0 else -1

print(bfs())