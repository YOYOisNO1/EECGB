def program475():
    
    a,b,c,n=map(int,input().split())
    
    if a<=n-1 and b<=n-1 and a-c>=0 and b-c>=0 :
        if n-(a+b-c)>0:
            print(n-(a+b-c))
    
        else:
            print(-1)
    
    else:
        print(-1)