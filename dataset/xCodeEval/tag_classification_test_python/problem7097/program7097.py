def program7097():
    p, k = map(int,input().split())
    
    c = 1000000007
    
    if k==0:
        answer = pow(p,p-1,c)
    elif k==1:
        answer = pow(p,p,c)
    else:
        size = 1
        nk = k
        while nk!=1:
            size+=1
            nk=(nk*k)%p
        cycles = (p-1)//size
        answer = pow(p,cycles,c)
    
    print(answer)