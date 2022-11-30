N = int(input())

W = 5*(N//3)+(N//3)-1
H = N
arr = [[' ']*W for _ in range(H)]

vectors = ((2,0),(1,1),(3,1),(0,2),(1,2),(2,2),(3,2),(4,2))

def recursion(x, y, w, h):
    if h==3:
        for vx, vy in vectors: arr[y+vy][x+vx] = '*'
        return
    vx = (w+1)//4
    vy = h//2
    recursion(x+vx, y, w//2, h//2)
    recursion(x, y+vy, w//2, h//2)
    recursion(x+vx*2, y+vy, w//2, h//2)

recursion(0, 0, W, H)

for i in map(lambda a: ''.join(a), arr):
    print(i)