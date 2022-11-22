from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    mapper = defaultdict(set)
    n = int(input())
    for _ in range(n):
        option, type = input().rstrip().split()
        mapper[type].add(option)
    ans = 1
    for n in list(map(lambda x:len(x)+1, mapper.values())):
        ans *= n
    print(ans-1)