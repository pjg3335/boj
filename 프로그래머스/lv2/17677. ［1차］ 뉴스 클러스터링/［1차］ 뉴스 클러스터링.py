from collections import defaultdict

def parse(string):
    arr = []
    for i in range(1, len(string)):
        arr.append(string[i-1:i+1].lower())
    return arr

def filter_alpha(arr):
    return list(filter(lambda string: string[0].isalpha() and string[1].isalpha() , arr))

def to_set(arr):
    dict = defaultdict(int)
    for e in arr:
        dict[e] += 1
    return dict

def i_len(s1, s2):
    cnt = 0
    for key in s1.keys():
        if s1[key] and s2[key]:
            cnt += min(s1[key], s2[key])
    return cnt

def u_len(s1, s2):
    cnt = 0
    for key in set(list(s1.keys())+list(s2.keys())):
        cnt += max(s1[key], s2[key])
    return cnt

def solution(str1, str2):
    answer = 0
    A = to_set(filter_alpha(parse(str1)))
    B = to_set(filter_alpha(parse(str2)))
    
    i = i_len(A, B)
    u = u_len(A, B)
    
    J = None
    if u == 0:
        J = 1
    else:
        J = i/u
        
    return int(65536*J)