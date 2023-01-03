import sys
sys.setrecursionlimit(10**9)

def solution(a, b, n, t=0):
    if n+t<a: return 0
    return (n+t)//a*b + solution(a, b, (n+t)//a*b, (n+t)%a)