while True:
    string = input()
    if string == '0': break
    
    for i in range(0, (len(string)+1)//2):
        if string[i] != string[len(string)-1-i]:
            print('no')
            break
    else:
        print('yes')