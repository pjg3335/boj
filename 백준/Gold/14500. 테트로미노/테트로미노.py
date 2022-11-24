import sys
input = sys.stdin.readline

tetrominos = (
    ((0,0),(1,0),(2,0),(3,0)), # I
    ((0,0),(0,1),(0,2),(0,3)), # I 90
    ((0,0),(0,1),(1,0),(1,1)), # O
    ((0,0),(0,1),(0,2),(1,2)), # L
    ((0,0),(1,0),(2,0),(0,1)), # L 90
    ((0,0),(1,0),(1,1),(1,2)), # L 180
    ((0,0),(1,0),(2,0),(2,-1)), # L 270
    ((0,0),(0,1),(1,1),(1,2)), # S
    ((0,0),(1,0),(1,-1),(2,-1)), # S 90
    ((0,0),(1,0),(2,0),(1,1)), # A
    ((0,0),(0,1),(0,2),(1,1)), # A 90
    ((0,0),(1,0),(2,0),(1,-1)), # A 180
    ((0,0),(0,1),(0,2),(-1,1)), # A 270
    ((0,0),(1,0),(1,-1),(1,-2)), # J
    ((0,0),(0,1),(1,1),(2,1)), # J 90
    ((0,0),(1,0),(0,1),(0,2)), # J 180
    ((0,0),(1,0),(2,0),(2,1)), # J 270
    ((0,0),(0,1),(-1,1),(-1,2)), # Z
    ((0,0),(1,0),(1,1),(2,1)), # Z 90
)

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

def get_sum(x, y, tetromino):
    sum = 0
    for vx, vy in tetromino:
        nx, ny = (x+vx, y+vy)
        if 0<=nx<M and 0<=ny<N:
            sum += arr[ny][nx]
        else:
            return 0
    return sum

ans = 0
for y in range(N):
    for x in range(M):
        for tetromino in tetrominos:
            ans = max(ans, get_sum(x, y, tetromino))
print(ans)