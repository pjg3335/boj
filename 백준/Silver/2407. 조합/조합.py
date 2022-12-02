n, m = map(int, input().split())

def mul(num, length):
    tmp = 1
    now_length = 0
    while now_length != length:
        tmp *= num
        num -= 1
        now_length += 1
    return tmp

print(mul(n, m)//mul(m, m))