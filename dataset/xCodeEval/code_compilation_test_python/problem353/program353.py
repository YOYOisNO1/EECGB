def program353():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t = 1
    while True:
        s = str(t)
        flag1 = False
        flag2 = False
        # print(t)
        for x in s:
            if int(x) in a:
                flag1 = True
            if int(x) in b:
                flag2 = True
            # print(x, flag1, flag2)
        if flag1 and flag2:
            break
        # t = t + 1
    
    print(t)