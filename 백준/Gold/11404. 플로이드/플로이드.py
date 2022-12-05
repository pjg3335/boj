import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())

dp = [[math.inf]*(n) for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    dp[a-1][b-1] = min(c, dp[a-1][b-1])


for m in range(n):
    for s in range(n):
        for e in range(n):
            if s!=e:
                dp[s][e] = min(dp[s][m]+dp[m][e], dp[s][e])

for arr in dp:
    print(" ".join(list(map(
        lambda x: str(x) if x!=math.inf else '0', 
        arr
    ))))