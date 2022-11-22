import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x==0:
        if len(heap):
            _, x = heapq.heappop(heap)
            print(x)
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
        