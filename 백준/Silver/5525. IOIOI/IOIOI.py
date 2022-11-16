N = int(input())
M = int(input())
string = list(input())

ans = 0
cnt = 0
for i in range(M):
    c = string[i]
    if c=='I' and cnt%2==0:
        cnt += 1
    elif c=='O' and cnt%2==1:
        cnt += 1
    
    if i+1>=M or (string[i+1]=='I' and cnt%2==1) or (string[i+1]=='O' and cnt%2==0):
        cnt -= N*2+1
        if cnt >= 0:
            ans += 1+cnt//2
        cnt = 0

print(ans)
