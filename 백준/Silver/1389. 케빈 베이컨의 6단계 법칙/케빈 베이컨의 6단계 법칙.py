import sys
from collections import defaultdict, deque 
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = graph[e][s] = True

def bfs(s):
    visited = [False]*(N+1)
    cnt = 0

    q = deque()
    q.append((s,0))
    visited[s] = True

    while q:
        s, d = q.popleft()
        for e in range(1, N+1):
            if not visited[e] and graph[s][e]:
                q.append((e,d+1))
                visited[e] = True
                cnt += d+1

    return cnt

max_cnt = 2**31
ans = -1
for s in range(1, N+1):
    cnt = bfs(s)
    if cnt < max_cnt:
        max_cnt = cnt
        ans = s

print(ans)