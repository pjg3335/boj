import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()

        for e in graph[s]:
            if not visited[e]:
                q.append(e)
                visited[e] = True

ans = 0
for s in range(1, N+1):
    if not visited[s]:
        ans += 1
        bfs(s)

print(ans)