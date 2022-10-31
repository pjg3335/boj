from math import gcd

def lcm(a, b):
    return int(a*b/gcd(a,b))

N, M = map(int, input().split())

print(gcd(N,M))
print(lcm(N,M))
