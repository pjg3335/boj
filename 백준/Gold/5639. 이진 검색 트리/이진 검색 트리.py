import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def recursion(s, e):
    if s>e: return

    root = arr[s]
    m = e+1
    for i in range(s+1, e+1):
        if root<arr[i]:
            m = i
            break

    recursion(s+1, m-1)
    recursion(m, e)
    print(root)

recursion(0, len(arr)-1)