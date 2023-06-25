def program109():
    f=[7,17,27,37,47,57]
    x=input()
    s=input()
    h,m=map(int,s.split())
    if '7' in s:
        print(0)
    else:
        t=h*60+m
        cnt=1
        while True:
            t=(t-x)%1440
            h,m=t/60,t%60
            if h in f or m in f:
                print(cnt)
                exit()
            else:
                cnt+=1
        print(cnt)