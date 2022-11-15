import sys
from collections import defaultdict, deque
input = sys.stdin.readline

com_cnt = int(input())
N = int(input())
graph = defaultdict(list)
for _ in range(N):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

def bfs(s):
    visited = [False]*(com_cnt+1)
    
    q = deque()
    q.append(s)
    visited[s] = True

    ans = 0
    while q:
        s = q.popleft()
        ans += 1
        for e in graph[s]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
    return ans

print(bfs(1)-1)