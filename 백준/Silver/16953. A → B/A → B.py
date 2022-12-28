from collections import deque, defaultdict

A, B = map(int, input().split())

def bfs(s, e):
    visited = defaultdict(bool)
    q = deque()
    q.append((s, 1))
    visited[s] = True

    while q:
        x, d = q.popleft()
        for nx in [x*2, int(str(x)+"1")]:
            nd = d+1
            if nx == e:
                return nd
            elif nx <= e and not visited[nx]:
                q.append((nx, nd))
                visited[nx] = True
    
    return -1

print(bfs(A, B))