import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

def find(a):
    if parent[a] == a: return a
    parent[a] = find(parent[a]) 
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b: parent[b] = a
    else: parent[a] = b

def is_same_parent(a, b):
    a = find(a)
    b = find(b)
    return a==b

parent = [i for i in range(N+1)]

known = list(map(int, input().rstrip().split()))[1:]
parties = [list(map(int, input().rstrip().split()))[1:] for _ in range(M)]
for party in [known]+parties:
    for i in range(1, len(party)):
        union(party[i-1], party[i])

cnt = 0
if len(known):
    for party in parties:
        if not is_same_parent(known[0], party[0]):
            cnt += 1
else:
    cnt = len(parties)
print(cnt)
