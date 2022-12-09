import sys
import math
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().rstrip().split())
    graph[s].append((d, e))
S, E = map(int, input().rstrip().split())

def dijkstra(S):
    dist = [math.inf]*(N+1)
    
    q = []
    dist[S] = 0
    heapq.heappush(q, (0, S))

    while q:
        td, s = heapq.heappop(q)
        
        if dist[s]<td: continue

        for nd, e in graph[s]:
            d = td+nd
            if dist[e]>d:
                heapq.heappush(q, (d, e))
                dist[e] = d

    return dist

print(dijkstra(S)[E])