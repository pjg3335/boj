import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque()
for _ in range(n): arr.append(int(input()))

stack = []
numbers = range(1, n+1)
ops = []

for n in numbers:
    ops.append('+')
    stack.append(n)
    while len(stack) and len(arr) and stack[len(stack)-1] == arr[0]:
        ops.append('-')
        stack.pop()
        arr.popleft()

if len(stack) == 0:
    for o in ops: print(o)
else:
    print('NO')


