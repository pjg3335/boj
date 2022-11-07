import sys
input = sys.stdin.readline

T = int(input())

arr = [[0]*15 for _ in range(15)]
for i in range(15): 
    arr[0][i] = i
    arr[i][1] = 1
for y in range(1, 15):
    for x in range(2, 15):
        arr[y][x] = arr[y][x-1]+arr[y-1][x]

for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])