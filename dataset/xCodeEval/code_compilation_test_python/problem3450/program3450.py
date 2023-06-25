def program3450():
    import numpy as np
    n,k = map(int,input().split(' '))
    count=0
    f=0
    factors=[]
    for i in range(2,n):
        while(count !=k-1 and n%i==0):
            count +=1
            factors.append(i)
            n=n//i
        factors.append(n)
        if(count ==k-1):
            f=1
            break
    
    if(f == 1 ):    
       
        print(*factors,sep=' ')
    else:
        print(-1)