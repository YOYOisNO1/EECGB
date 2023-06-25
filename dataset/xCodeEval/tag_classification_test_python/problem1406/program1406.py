def program1406():
    k1,n1,w1=input().split()
    k=int(k1)
    n=int(n1)
    m=n
    w=int(w1)
    mused=0
    count=1
    p=0
    i=w
    while i>0:
        mused=count*k
        n=n-mused
        i=i-1
        count=count+1
    
    
    if n<0:
        print(-1*n)
    else:
        print('0')