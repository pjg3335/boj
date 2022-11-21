import sys
import heapq
input = sys.stdin.readline

def sync(q):
    while q and not valids[q[0][1]]:
        heapq.heappop(q)

T = int(input())
for _ in range(T):
    k = int(input())
    valids = [False]*k
    min_q = []
    max_q = []
    for i in range(k):
        o, n = input().split()
        n = int(n)
        if o=='I':
            heapq.heappush(min_q, (n, i))
            heapq.heappush(max_q, (-n, i))
            valids[i] = True
        elif n==-1:
            sync(min_q)
            if min_q:
                _, id = heapq.heappop(min_q)
                valids[id] = False
        else:
            sync(max_q)
            if max_q:
                _, id = heapq.heappop(max_q)
                valids[id] = False
    sync(max_q)
    sync(min_q)
    if len(max_q):
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')
