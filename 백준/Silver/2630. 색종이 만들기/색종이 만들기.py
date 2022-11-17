import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

def recursion(arr, size, x, y):
    if size == 1:
        if arr[y][x]==1: return (0,1)
        else: return (1,0)

    nsize = size//2
    w1, b1 = recursion(arr, nsize, x, y)
    w2, b2 = recursion(arr, nsize, x+nsize, y)
    w3, b3 = recursion(arr, nsize, x, y+nsize)
    w4, b4 = recursion(arr, nsize, x+nsize, y+nsize)
    
    w = w1+w2+w3+w4
    b = b1+b2+b3+b4

    if w==0: return (0, 1)
    elif b==0: return (1,0)
    else: return (w, b)

w, b = recursion(arr, N, 0, 0)
print(w)
print(b)