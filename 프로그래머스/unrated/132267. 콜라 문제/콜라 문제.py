import sys
sys.setrecursionlimit(10**9)

def solution(a, b, n):
    return 0 if n<a else n//a*b + solution(a, b, n//a*b+n%a)