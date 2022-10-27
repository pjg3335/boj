from collections import defaultdict

string = input().upper()
obj = defaultdict(int)
for c in string: obj[c] += 1
mx = max(obj.values())
mx_cnt = list(obj.values()).count(mx)

if mx_cnt != 1: print('?')
else:
    for k in obj:
        if obj[k] == mx:
            print(k)
            break
