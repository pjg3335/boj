import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N = int(input())
arr = [input().rstrip() for _ in range(N)]

def recursion(arr, s, x, y):
    if s==1: return arr[y][x]

    ns = s//2
    a1 = recursion(arr, ns, x, y)
    a2 = recursion(arr, ns, x+ns, y)
    a3 = recursion(arr, ns, x, y+ns)
    a4 = recursion(arr, ns, x+ns, y+ns)
    if len(a1)==1 and a1 == a2 and a1 == a3 and a1 == a4:
        return a1
    else:
        return '('+a1+a2+a3+a4+')'

print(recursion(arr, N, 0, 0))