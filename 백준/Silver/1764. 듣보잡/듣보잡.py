import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = set()
b = set()

for _ in range(N): d.add(input().rstrip())
for _ in range(M): b.add(input().rstrip())

db = d & b
print(len(db))
for dbj in sorted(list(db)): print(dbj)