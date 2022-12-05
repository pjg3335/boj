N = int(input())

def recursion(n, s, e, t):
    if n==1:
        print(s, e)
        return
    recursion(n-1, s, t, e)
    print(s, e)
    recursion(n-1, t, e, s)

print(2**N-1)
recursion(N, 1, 3, 2)
