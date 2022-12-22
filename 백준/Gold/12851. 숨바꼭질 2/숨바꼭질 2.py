from collections import deque

N, K = map(int, input().split())

def bfs(s):
    visited_d = [-1]*100_001
    q = deque()
    q.append((s,0))
    visited_d[s] = 0

    cnt = 0

    while q:
        s, d = q.popleft()
        if s == K:
            cnt += 1
            continue
        if visited_d[K] != -1 and visited_d[K]<d:
            continue

        for e in [s-1, s+1, s*2]:
            if 0<=e<100_001:
                if visited_d[e] == -1 or visited_d[e] == d+1:
                    visited_d[e] = d+1
                    q.append((e, d+1))
                    
    return (visited_d[K], cnt)

d, cnt = bfs(N)
print(d)
print(cnt)