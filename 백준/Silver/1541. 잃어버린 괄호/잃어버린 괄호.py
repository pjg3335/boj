nums = list(map(
    lambda s: sum(map(int, s.split('+'))), 
    input().split('-')
))
print(nums[0]-sum(nums[1:]))
