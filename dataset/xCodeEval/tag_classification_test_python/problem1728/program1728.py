def program1728():
    n,k=map(int,input().split())
    if n==1 and k==10:
        print(-1)
    else:
        m = pow(10,n-1,k)
        mm = pow(10,n-1)
        
        
        print(mm+(k-m))