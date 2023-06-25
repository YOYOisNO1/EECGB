def program209():
    a,b = map(int, input().strip().split(':'))
    f = {
        0:0,
        1:10,
        2:20,
        3:30,
        4:40,
        5:50,
        10:01,
        11:11,
        12:21,
        13:31,
        14:41,
        15:51,
        20:02,
        21:12,
        22:22,
        23:32
    }
    if a in f:
        d = f[a]
        if b <= d:
            print(d-b)
        else:
            k = a+1
            if k in f:
                print(60-b+f[k])
            else:
                if k==6:
                    print(60-b) + 241
                elif k == 16:
                    print(60-b) + 242
                elif k == 24:
                    print(60-b)
    else:
        if a < 10 and a > 5:
            j = 10-(a+1)
            print(j*60) + (60-b) + 1
        elif a < 20 and a>15:
            j = 20 - (a+1)
            print(j*60) + (60-b) + 2
        
    