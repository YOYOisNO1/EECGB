def program3947():
    n,m = map(int,input().split())
    if ((n**101-1)/(n-1)) < m:
        print('NO')
        quit()
    
    while m != 0:
        if (m-1)%n == 0:
            m = (m-1)/n
        elif (m+1)%n == 0:
            m = (m+1)/n
        elif m%n == 0:
            m = m/n 
        else:
            print('NO')
            quit()
    
    print('YES')