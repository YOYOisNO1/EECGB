def program699():
    n,m=map(int,input().split())
    
    x=(n*(n+1))//2
    
    y=m%x
    
    for i in range(1,n+1):
        y-=i
     
        if y<0:
            print(i+y)
            break
        elif y==0:
            print(0)
            break
        else:
            continue