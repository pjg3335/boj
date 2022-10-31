def is_prime(num):
    if num == 1: return False
    for i in range(2, num):
        if num%i==0: return False
    return True

N = int(input())
arr = list(map(is_prime, map(int, input().split())))

print(arr.count(True))
