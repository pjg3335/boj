A = int(input())
B = int(input())
C = int(input())
ans = [0]*10
for n in str(A*B*C): ans[int(n)] += 1
for c in ans: print(c)