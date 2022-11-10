import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = defaultdict(bool)
for _ in range(M):
    s, e = map(int, input().split())
    graph[(s,e)] = graph[(e,s)] = True

def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        s = q.popleft()
        print(s, end=' ')

        for e in range(1, N+1):
            if not visited[e] and graph[(s,e)]:
                q.append(e)
                visited[e] = True

def dfs(s):
    print(s, end=' ')
    visited[s] = True

    for e in range(1, N+1):
        if not visited[e] and graph[(s,e)]:
            dfs(e)

visited = [False]*(N+1)
dfs(V)
print()
visited = [False]*(N+1)
bfs(V)