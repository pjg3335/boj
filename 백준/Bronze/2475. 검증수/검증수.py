arr = list(map(lambda n:n**2, map(int, input().split())))
print(sum(arr)%10)