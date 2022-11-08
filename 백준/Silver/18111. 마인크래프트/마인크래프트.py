import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

min_time = 2**31
max_y = 0

for y in range(256,-1,-1):
    block_cnt = B
    time = 0

    for w in range(M):
        for h in range(N):
            diff = arr[h][w] - y
            if diff > 0:
                time += diff*2
            elif diff < 0:
                time -= diff
            block_cnt += diff
    
    if block_cnt >= 0 and time < min_time:
        max_y = y
        min_time = time

print(min_time, max_y)