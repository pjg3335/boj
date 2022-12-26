from collections import deque

L = 102

def draw_rect(arr, rectangle):
    sx, sy, ex, ey = map(lambda x:x*2, rectangle)
    for x in range(sx, ex+1):
        arr[sy][x] = 1
        arr[ey][x] = 1
    for y in range(sy, ey+1):
        arr[y][sx] = 1
        arr[y][ex] = 1

def make_road(arr):
    visited = [[False]*L for _ in range(L)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    vectors = ((0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1))
    
    while q:
        x, y = q.popleft()
        for vx, vy in vectors:
            nx, ny = (x+vx, y+vy)
            if 0<=nx<L and 0<=ny<L and not visited[ny][nx]:
                if arr[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((nx, ny))
                elif arr[ny][nx] == 1:
                    arr[ny][nx] = 2

def bfs(arr, sx, sy, ex, ey):
    visited = [[False]*L for _ in range(L)]
    q = deque()
    q.append((sx, sy, 0))
    visited[sy][sx] = True
    vectors = ((0,1),(0,-1),(1,0),(-1,0))
      
    while q:
        x, y, d = q.popleft()
        for vx, vy in vectors:
            nx, ny, nd = (x+vx, y+vy, d+1)
            if 0<=nx<L and 0<=ny<L and not visited[ny][nx] and arr[ny][nx] == 2:
                if nx == ex and ny == ey:
                    return nd//2
                visited[ny][nx] = True
                q.append((nx, ny, nd))

def solution(rectangles, characterX, characterY, itemX, itemY):
    arr = [[0]*L for _ in range(L)]
    for rectangle in rectangles:
        draw_rect(arr, rectangle)
    make_road(arr)
    ans = bfs(arr, characterX*2, characterY*2, itemX*2, itemY*2)
    return ans