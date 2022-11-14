import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = int(input())
    if x==0:
        if len(q): print(heapq.heappop(q))
        else: print(0)
    else:
        heapq.heappush(q, x)
