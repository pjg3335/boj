A, B = map(int, map(lambda s:"".join(reversed(s)), input().split()))
if A>B:
    print(A)
else:
    print(B)

