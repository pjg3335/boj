import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for _ in range(N):
    o = sys.stdin.readline()
    if o.startswith('push_back'):
        q.append(int(o.replace('push_back ', '')))
    elif o.startswith('push_front'):
        q.appendleft(int(o.replace('push_front ', '')))
    elif o.startswith('pop_front'):
        if len(q) == 0: print(-1)
        else: print(q.popleft())
    elif o.startswith('pop_back'):
        if len(q) == 0: print(-1)
        else: print(q.pop())
    elif o.startswith('size'):
        print(len(q))
    elif o.startswith('empty'):
        if len(q) == 0: print(1)
        else: print(0)
    elif o.startswith('front'):
        if len(q) == 0: print(-1)
        else: print(q[0])
    elif o.startswith('back'):
        if len(q) == 0: print(-1)
        else: print(q[len(q)-1])