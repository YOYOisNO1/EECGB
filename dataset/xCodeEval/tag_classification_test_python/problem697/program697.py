def program697():
    n,m=map(int,input().split())
    i=0
    while((m-i)>=0):
        for i in range(1,n+1):
            if m-i>=0:
                m=m-i
            else:
                break
            if(i==n):
                i=1
                break
    print(m)
        
        
        