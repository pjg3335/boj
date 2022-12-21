string = list(input())
bomb = list(input())

stack = []
for c in string:
    stack.append(c)
    if c==bomb[-1] and len(stack)>=len(bomb) and stack[-len(bomb):]==bomb:
        for _ in range(len(bomb)):
            stack.pop()

ans = "".join(stack)
if ans == "":
    print('FRULA')
else:
    print(ans)
