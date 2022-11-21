from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (2*n)%10000
def S(n):
    return 9999 if n==0 else n-1
def L(n):
    return n%1000*10+n//1000
def R(n):
    return n%10*1000+n//10

orders = {'D':D, 'S':S, 'L':L, 'R':R,}

def bfs(A, B):
    visited = set()
    q = deque()
    q.append((A, ''))
    visited.add(A)

    while q:
        n, o = q.popleft()
        if n==B: return o
        for key in orders.keys():
            nn = orders[key](n)
            no = o+key
            if nn not in visited:
                q.append((nn, no))
                visited.add(nn)

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(bfs(A, B))
    