N = int(input())
arr = [[' ']*(N*2-1) for _ in range(N)]
vectors = ((2,0),(1,1),(3,1),(0,2),(1,2),(2,2),(3,2),(4,2))

def recursion(x, y, h):
    if h==3:
        for vx, vy in vectors: arr[y+vy][x+vx] = '*'
        return
    h = h//2
    recursion(x+h, y, h)
    recursion(x, y+h, h)
    recursion(x+h*2, y+h, h)

recursion(0, 0, N)

for a in arr:
    print(''.join(a))