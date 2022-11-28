import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
graph = defaultdict(list)
for _ in range(N):
    s, l, r = input().rstrip().split()
    graph[s].append(l)
    graph[s].append(r)
visited = defaultdict(bool)
traversal = [[],[],[]]

def recursion(s):
    visited[s] = True
    l, r = graph[s]
    
    traversal[0].append(s)
    if not visited[l] and l != '.': recursion(l)
    traversal[1].append(s)
    if not visited[r] and r != '.': recursion(r)
    traversal[2].append(s)

recursion('A')
traversal = list(map(lambda arr: ''.join(arr), traversal))
for t in traversal: print(t)