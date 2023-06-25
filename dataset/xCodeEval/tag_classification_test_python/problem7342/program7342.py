def program7342():
    N,M = map(int,input().split())
    l = [0,1,2,3,2,1]
    
    res = float('inf')
    
    for (n,m) in ((N,M),(M,N)):
        if l[n%6]==0:
            print(n*m)
            exit()
        elif l[n%6]==1:
            tmp = l[m%6]
            res = min(res,tmp)
        elif l[n%6]==2:
            if m>=4 and m!=7:
                print(n*m)
                exit()
            if m==2:
                tmp = 4
            else:
                tmp = 2
            res = min(res,tmp)
        else:
            if m==1:
                tmp = 3
            elif m==2:
                tmp = 2
            elif m%2==0:
                print(n*m)
                exit()
            else:
                tmp = 1
            res = min(res,tmp)
    
    print(n*m-res)