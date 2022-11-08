import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.': break

    stack = []
    pairs = (('(',')'), ('[',']'))
    condition = True

    for c in string:
        if not condition: break

        for s, e in pairs:
            if c == s: 
                stack.append(c)
            elif c == e:
                if len(stack) != 0 and s == stack[-1]:
                    stack.pop()
                else:
                    condition = False

    print('yes' if not stack and condition else 'no')
