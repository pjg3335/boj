import sys
import math
input = sys.stdin.readline

def bf(s):
    dist = [10001]*(N+1)
    dist[s] = 0
    
    for used_edge_cnt in range(1, N+1):
        for s in range(1, N+1):
            for e, d in graph[s]:
                if dist[e]>dist[s]+d:
                    dist[e] = dist[s]+d
                    if used_edge_cnt == N:
                        return (False, [-math.inf]*(N+1))

    return (True, dist)

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().rstrip().split())
    graph = [[] for _ in range(N+1)]
    
    for _ in range(M):
        S, E, T = map(int, input().rstrip().split())
        graph[S].append((E, T))
        graph[E].append((S, T))
        
    for _ in range(W):
        S, E, T = map(int, input().rstrip().split())
        graph[S].append((E, -T))

    valid, dist = bf(1)

    if valid:
        print('NO')
    else:
        print('YES')