N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def recursive(array, r):
	for i in range(len(array)):
		if r == 1:
			yield [array[i]]
		else:
			for next in recursive(array[:i] + array[i+1:], r-1):
				yield [array[i]] + next

s = set()
for i in recursive(arr, M):
    if str(i) not in s:
        print(" ".join(list(map(str, i))))
        s.add(str(i))