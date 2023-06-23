    import math
def c(k,n):
        return (k-1)*(k-1)+(n-k*2+1)*(n-k*2)/2+(k*2-1)*(n-k*2+1)
    
    n,m,k=list(map(int,input().split()))
    m=m-n
    if k>n/2:
        k=n-k+1
    
    if k*k>=m:
        if int(m**0.2)=m**0.2:
            print(int(m**0.2))
        else:
            print(int(m**0.2)+1)
        exit()
    elif c(k,n)>=m:
        #m=m-(k-1)*(k-1)
        #for i in range(n+5):
        #    if i*((i-1)/2+k*2)>m:
        #        print(i+k)
        #        exit()
        m=m-(k-1)*(k-1)
        x=k-1
        for i in range(n+5):
            if i+k*2-1>m:
                print(i+x+1)
                exit()
            m=m-i-k*2+1
    else:
        m=m-c(k,n)
        print(int(m//n+n-k+1))