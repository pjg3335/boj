import sys
N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    o = sys.stdin.readline()
    if o.startswith('push'):
        stack.append(int(o.replace('push ', '')))
    elif o.startswith('pop'):
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif o.startswith('size'):
        print(len(stack))
    elif o.startswith('empty'):
        if len(stack) == 0: print(1)
        else: print(0)
    elif o.startswith('top'):
        if len(stack) == 0: print(-1)
        else: print(stack[len(stack)-1])