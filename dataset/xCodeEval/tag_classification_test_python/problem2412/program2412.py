def program2412():
    n, s = int(input()), input()
    ma, num, flag, flag2, c = [0 for i in range(5)]
    
    for i in s:
        if i == '(' or i == ')':
            flag = not (flag)
            flag2 = 0
            c = 0
        elif flag:
            if i == '_':
                flag2 = 0
            elif flag2 == 0:
                num += 1
                flag2 = 1
        elif i == '_':
            c = 0
        else:
            c += 1
            ma = max(c, ma)
    
    print(ma, num)