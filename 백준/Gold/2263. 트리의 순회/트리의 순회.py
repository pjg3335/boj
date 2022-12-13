import sys
sys.setrecursionlimit(1000000)

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_order_pos = [-1]*(n+1)
for i in range(n):
    in_order_pos[in_order[i]] = i

def recursive(in_s, in_e, p_s, p_e):
    if in_s>in_e or p_s>p_e: return

    root = post_order[p_e]
    print(root, end=" ")

    root_idx = in_order_pos[root]
    left_len = root_idx-in_s

    recursive(in_s, in_s+left_len-1, p_s, p_s+left_len-1)
    recursive(in_s+left_len+1, in_e, p_s+left_len, p_e-1)

recursive(0, n-1, 0, n-1)