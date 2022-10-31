T = int(input())

for _ in range(T):
    string = input()

    open_cnt = 0
    for c in string:
        if c=='(':
            open_cnt += 1
        elif c==')' and open_cnt>0:
            open_cnt -= 1
        else:
            print('NO')
            break
    else:
        if open_cnt == 0: print('YES')
        else: print('NO')