while True:
    nums = list(map(int, input().split()))
    if nums.count(0) == 3: break

    a,b,c = sorted(nums)
    if a**2+b**2 == c**2:
        print('right')
    else:
        print('wrong')