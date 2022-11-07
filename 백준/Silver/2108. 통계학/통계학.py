import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

avg = round(sum(arr)/N)
med = arr[N//2]
ran = arr[N-1]-arr[0]

counter = defaultdict(int)
for n in arr: counter[n] += 1
arr = []
for key in counter: arr.append((counter[key], key))
arr = sorted(arr, key=lambda n: (n[0], -n[1]))
mod = arr[len(arr)-1][1] if len(arr)==1 or arr[len(arr)-1][0] != arr[len(arr)-2][0] else arr[len(arr)-2][1]

print(avg)
print(med)
print(mod)
print(ran)