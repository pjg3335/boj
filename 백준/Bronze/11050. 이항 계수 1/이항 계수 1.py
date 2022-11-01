N, K = map(int, input().split())
def mul(arr):
    tmp = 1
    for n in arr:
        tmp*=n
    return tmp

print(int(mul(range(N-K+1, N+1))/mul(range(1, K+1))))