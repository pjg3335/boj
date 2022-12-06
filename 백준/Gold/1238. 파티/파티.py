import sys
import heapq
import math
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split())
graph = [[] for _  in range(N+1)]
r_graph = [[] for _  in range(N+1)]

for _ in range(M):
    s, e, T = map(int, input().rstrip().split())
    graph[s].append((T, e))
    r_graph[e].append((T, s))

def dijkstra(graph, s):
    distance = [math.inf]*(N+1)
    distance[s] = 0

    q = []
    heapq.heappush(q, (0, s))

    while q:
        sT, s = heapq.heappop(q)

        if distance[s] < sT: continue

        for eT, e in graph[s]:
            if distance[e]>sT+eT:
                distance[e] = sT+eT
                heapq.heappush(q, (distance[e], e))
    
    return distance

distance = dijkstra(graph, X)
r_distance =  dijkstra(r_graph, X)
ans = 0
for e in range(1, N+1):
    ans = max(ans, distance[e]+r_distance[e])

print(ans)