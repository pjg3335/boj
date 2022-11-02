N = int(input())

cnt = 0
now = 665
while True:
    now += 1
    if "666" in str(now): cnt+=1
    if cnt == N: break
print(now)