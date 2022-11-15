import sys
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    s, e = map(int, input().split())
    q.append((s,e))
q.sort(key=lambda x:(x[1], x[0]))
prev_e = 0
ans = 0
for s, e in q:
    if s >= prev_e:
        ans += 1
        prev_e = e
print(ans)