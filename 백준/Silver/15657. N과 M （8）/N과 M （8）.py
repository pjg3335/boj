N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def recursive(arr, depth, tmp = []):
    if depth == 0:
        print(" ".join(list(map(str, tmp))))
    else:
        for e in arr:
            if len(tmp) == 0 or e>=tmp[-1]:
                recursive(arr, depth-1, tmp+[e])

recursive(arr, M)