N = int(input())

cnt = 1
tmp = 1
while N > tmp:
    tmp += 6*cnt
    cnt += 1
print(cnt)