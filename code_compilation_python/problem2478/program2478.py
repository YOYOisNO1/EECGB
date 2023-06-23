def program2478():
    #from dust i have come, dust i will be
    
    n=int(input())
    
    hv=[0]*9
    
    xn=str(n)
    for i in range(len(xn)):
        hv[int(xn[i])]=1
    
    cnt=1
    for i in range(1,n):
        if n%i==0:
            yn=str(i)
            for j in range(len(yn)):
                if hv[int(yn[j])]==1:
                    cnt+=1
                    break
    
    print(cnt)
    
    
    
    
    
    
    