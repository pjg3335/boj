string = list(input())

stack = []
res = ''
for c in string:
    if c.isalpha():
        res += c
    else:
        if c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()

print(res)
