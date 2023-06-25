def program3912():
    w,m=map(int,input().split())
    f=0
    ff=0
    while m!=0:
        i=0
        ma=0
        while w**i<m:
            ma+=w**i
            i+=1
        if w**i-ma<=m:# and ff!=2:
            ff=1
            m=w**i-m
        elif ma>=m:
            ff=2
            m=m-(w**(i-1))
        else:
            f=1
            print('NO')
            break
    if not f:
        print('YES')