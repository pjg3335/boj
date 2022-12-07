import sys
import heapq
import math
input = sys.stdin.readline

V, E = map(int, input().rstrip().split())
graph = [[] for _ in range(V+1)]

K = int(input())
for _ in range(E):
    s, e, d = map(int, input().rstrip().split())
    graph[s].append((d, e))

def dijkstra(s):
    distance = [math.inf]*(V+1)
    
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        pd, s = heapq.heappop(q)

        if pd>distance[s]: continue

        for nd, e in graph[s]:
            d = pd + nd
            if distance[e]>d:
                heapq.heappush(q, (d, e))
                distance[e] = d
    
    return distance

for i in dijkstra(K)[1:]:
    if i == math.inf: print('INF')
    else: print(i)