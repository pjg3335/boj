# 문제 상태 왜이러냐;
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mapper = {}
for i in range(1, N+1):
    name = input().rstrip() 
    mapper[name] = i
    mapper[str(i)] = name

for _ in range(M):
    inp = input().rstrip()
    print(mapper[inp])
