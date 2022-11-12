N = int(input())

def factorial(n):
    tmp = 1
    for i in range(1, n+1): tmp *= i
    return tmp

ans = 0
num = str(factorial(N))
for i in range(len(num)-1, 0, -1):
    if num[i] != '0': break
    ans += 1

print(ans)
