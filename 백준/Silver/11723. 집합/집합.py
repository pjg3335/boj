import sys
input = sys.stdin.readline

M = int(input())
s = set()
for _ in range(M):
    o = input().rstrip()
    if o=='all':
        s = set(range(1, 21))
    elif o=='empty':
        s = set()
    else:
        o, x = o.split()
        x = int(x)
        if o=='add':
            s.add(x)
        elif o=='remove':
            s.discard(x)
        elif o=='check':
            if x in s: print(1)
            else: print(0)
        elif o=='toggle':
            if x in s: s.remove(x)
            else: s.add(x)
