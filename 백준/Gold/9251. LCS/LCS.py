a = list(input())
b = list(input())

dp = [0]*len(a)

for c in b:
    tmp = 0
    for i in range(len(a)):
        if tmp < dp[i]:
            tmp = dp[i]
        elif c == a[i]:
            dp[i] = tmp+1

print(max(dp))
