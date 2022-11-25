import math

n = int(input())

dp = [math.inf]*(n+1)
dp[0], dp[1] = (0, 1)

for now in range(2, len(dp)):
    for prev in range(int(math.sqrt(now))+1):
        dp[now] = min(dp[now-prev**2]+1, dp[now])

print(dp[n])