def mod(a, m) : 
        return pow(a, m - 2, m) 
    
    
    a,b,n,x=list(map(int,input().split()))
    m=10**9+7
    if a==1:
        print((x+b*n)%m)
    else:
        print(int((pow(a,n,m)*x+(b*(pow(a,n,m)-1)*mod(a-1,m)))%m))