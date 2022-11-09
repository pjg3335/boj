import sys
sys.setrecursionlimit(10000)

N, r, c = map(int, input().split())

def dfs(size, x, y, acc=0):
    if size == 1: 
        return acc
    
    offset = int(size/4*size)
    half_size = int(size/2)
    if half_size < x+1: 
        acc += offset
        x -= half_size
    if half_size < y+1: 
        acc += offset*2
        y -= half_size
    return dfs(half_size, x, y, acc)

print(dfs(2**N, c, r))