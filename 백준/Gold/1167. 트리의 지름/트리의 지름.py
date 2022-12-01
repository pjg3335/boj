import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N):
    tmp = list(map(int, input().rstrip().split()))
    s = tmp[0]
    for i in range(1, len(tmp)-2, 2):
        e, d = (tmp[i], tmp[i+1])
        graph[s].append((e, d))

def bfs(s):
    visited = [False]*(N+1)
    q = deque()
    q.append((s, 0))
    visited[s] = True
    max_s = s
    max_d = 0

    while q:
        s, total_d = q.popleft()
        if max_d < total_d:
            max_s = s
            max_d = total_d
        for e, d in graph[s]:
            if not visited[e]:
                q.append((e, total_d+d))
                visited[e] = True
    
    return (max_s, max_d)

max_s, max_d = bfs(1)
max_s, max_d = bfs(max_s)

print(max_d)