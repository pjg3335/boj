import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

start = 1
end = 2**31-1

while start <= end:
    mid = (end+start)//2
    cnt = 0
    for e in arr: cnt += e//mid
    if cnt>=K:
        start = mid+1
    else:
        end = mid-1

print(end)
