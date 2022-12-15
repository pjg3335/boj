import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
vectors = ((1,0), (-1,0), (0,1), (0,-1))
cheese_cnt = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            cheese_cnt += 1

def melt():
    global cheese_cnt
    visited = [[False]*M for _ in range(N)]

    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    cheese = []

    while q:
        x, y = q.popleft()
        for vx, vy in vectors:
            nx, ny = (x+vx, y+vy)
            if 0<=nx<M and 0<=ny<N and not visited[ny][nx]:
                visited[ny][nx] = True
                is_cheese = arr[ny][nx] == 1
                if is_cheese:
                    cheese.append((nx, ny))
                else:
                    q.append((nx, ny))

    outside_cheese = []
    for x, y in cheese:
        empty_cnt = 0
        for vx, vy in vectors:
            nx, ny = (x+vx, y+vy)
            is_cheese = arr[ny][nx] == 1
            if visited[ny][nx] and not is_cheese:
                empty_cnt += 1
        if empty_cnt >= 2:
            outside_cheese.append((x, y))
            cheese_cnt -= 1
    
    for x, y in outside_cheese:
        arr[y][x] = 0

ans = 0
while cheese_cnt != 0:
    melt()
    ans += 1
print(ans)