A, B, C = map(int, input().rstrip().split())

def recursion(n, x):
    if x==1: return n%C
    n2 = recursion(n, x//2)
    return n2*n2*(n if x%2 else 1)%C

print(recursion(A, B))
