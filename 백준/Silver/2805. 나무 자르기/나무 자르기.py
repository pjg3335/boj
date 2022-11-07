N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = 2000000000
while start<=end:
    mid = (start+end)//2
    length = 0

    for tree in trees:
        length += max(0, tree-mid)
    
    if length>=M:
        start = mid+1
    else:
        end = mid-1

print(end)