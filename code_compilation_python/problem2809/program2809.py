def program2809():
    s = []
    for i in range(8):
        s.append(input())
    num = 0
    for i in s:
        if i == 'BBBBBBBB':
            num = num + 1
        else:
            num = 0
        else:
            w = i
            
    if num == 8:
        print(8)
    else:
        for i in w:
            if i == 'B':
                num = num + 1
        print(num)