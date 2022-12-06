import sys
import heapq
import math
input = sys.stdin.readline

N, E = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
v1, v2 = map(int, input().rstrip().split())

def dijkstra(s):
    distance = [math.inf]*(N+1)
    distance[s] = 0
    
    q = []
    heapq.heappush(q, (0, s))

    while q:
        sd, s = heapq.heappop(q)

        if distance[s]<sd: continue
        
        for ed, e in graph[s]:
            d = sd+ed
            if distance[e]>d:
                distance[e] = d
                heapq.heappush(q, (d, e))
    
    return distance

sd = dijkstra(1)
v1d = dijkstra(v1)
v2d = dijkstra(v2)

d = min(sd[v1]+v1d[v2]+v2d[N], sd[v2]+v2d[v1]+v1d[N])
if d == math.inf:
    print(-1)
else:
    print(d)