def program1663():
    n,m=map(int,input().split())
    if n<m:
        n,m=m,n
    
    if n-1+m-1<3:
        print(0)
        exit()
    
    if m==1:
        print(n-abs(abs(n%6-3)-3))
        exit()
    if m==2 and n==3:
        print(4)
        exit()
    if m==2 and n==7:
        print(12)
        exit()
    print(n*m-(n*m)%2)
    exit()
    
    
    if n%4==0 and m%4==0:
        print(n*m)
        exit()
    
    
    
    