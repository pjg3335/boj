from collections import deque

def bfs(arr, sx, sy):
    W = len(arr[0])
    H = len(arr)
    vectors = ((0,1),(0,-1),(1,0),(-1,0))
    visited = [[False]*W for _ in range(H)]
    
    q = deque()
    q.append((sx, sy, 1))
    visited[sy][sx] = True
    
    while q:
        x, y, d = q.popleft()
        for vx, vy in vectors:
            nx, ny, nd = (x+vx, y+vy, d+1)
            if 0<=nx<W and 0<=ny<H and not visited[ny][nx] and arr[ny][nx] == 1:
                if nx == W-1 and ny == H-1: 
                    return nd
                visited[ny][nx] = True
                q.append((nx, ny, nd))
                
    return -1
            
def solution(arr):
    return bfs(arr, 0, 0)