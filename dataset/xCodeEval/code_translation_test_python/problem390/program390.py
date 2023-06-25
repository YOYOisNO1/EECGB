def program390():
    num = input()
    cnt = 0
    flag = False
    for i in num:
        if i == '0'and flag:
            cnt += 1
        elif i == '1':
            flag = True
    if cnt >= 6:
        print('yes')
    else:
        print('no')
    