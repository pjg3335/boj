import sys
import math
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip().split()))]

mx_dp = arr[0]
mn_dp = arr[0]

for _ in range(N-1):
    a, b, c = list(map(int, input().rstrip().split()))
    mx_dp = [
        a+max(mx_dp[0], mx_dp[1]), 
        b+max(mx_dp[0], mx_dp[1], mx_dp[2]),
        c+max(mx_dp[1], mx_dp[2]),
    ]
    mn_dp = [
        a+min(mn_dp[0], mn_dp[1]),
        b+min(mn_dp[0], mn_dp[1], mn_dp[2]),
        c+min(mn_dp[1], mn_dp[2]),
    ]

print(max(mx_dp), min(mn_dp))