from collections import defaultdict, deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    counter = defaultdict(int)
    for e in arr: counter[e] += 1
    for i in range(2, 9+1): counter[i] += counter[i-1]

    arr = deque(map(lambda e: (False, e, counter[e]), arr))
    arr[M] = (True, arr[M][1], arr[M][2])

    for mn in range(len(arr), 0, -1):
        while len(arr) and arr[0][2] < mn:
            arr.append(arr.popleft())
        t, n, o = arr.popleft()
        if t:
            print(N-mn+1)
            break
