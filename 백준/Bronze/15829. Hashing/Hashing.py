L = int(input())
string = input()
r = 31
M = 1234567891

ans = 0
for i in range(L):
    a = ord(string[i])-96
    ans = (ans+a*(r**i))%M
print(ans)