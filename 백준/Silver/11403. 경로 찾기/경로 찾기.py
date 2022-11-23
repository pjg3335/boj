import sys
input = sys.stdin.readline

N = int(input())
dp = [list(map(int, input().rstrip().split())) for _ in range(N)]

for i in range(N):
    for x in range(N):
        for y in range(N):
            if dp[y][x]==0:
                if dp[y][i]==1 and dp[i][x]==1:
                    dp[y][x] = 1

print("\n".join(map(
    lambda arr: " ".join(map(
        lambda e: str(e), arr
    )), 
    dp))
)
