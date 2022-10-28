H, M = map(int, input().split())
h = H if M>=45 else (24+H-1)%24
m = (60+M-45)%60
print(h, m)