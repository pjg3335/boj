import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e, d = map(int, input().rstrip().split())
    tree[s].append((d, e))
    tree[e].append((d, s))

def bfs(s):
    visited = [False] * (n+1)
    
    q = deque()
    q.append((s, 0))
    visited[s] = True
    mx_node, mx_d = (s, 0)

    while q:
        s, sd = q.popleft()
        for nd, e in tree[s]:
            if not visited[e]:
                d = sd+nd
                visited[e] = True
                q.append((e, d))
                if mx_d<d:
                    mx_d = d
                    mx_node = e

    return (mx_node, mx_d)

node, dist = bfs(1)
node, dist = bfs(node)

print(dist)