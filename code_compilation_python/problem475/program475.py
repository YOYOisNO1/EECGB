def prime(m):
        f=0
        for i in range(2,m)):
            if (m % i) == 0: 
                break
        else: 
                f=1 
        return f
    
    import math
    c=0    
    n=int(input())
    for i in range(1,n):
        if(prime(n*i+1)==0):
            break
    print(i)