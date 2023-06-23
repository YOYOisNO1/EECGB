def program686():
    while True:
        try:
            x=input()
            y=map(int,input().split())
            if y[-1]==15:
                print 'DOWN'
            elif x==1:
                if y[0]==1：
                    print 'UP'
                else
                    print '-1'
            elif y[-1]>y[-2]:
                print 'UP'
            else:
                print 'DOWN'
        except:
            break