def lost(n,l,r):
        sum1=0
        sum2=0
        for i in range(r):
            sum2=sum2+(2**i)
        sum2=sum2+((n-r)*(2**(r-1))
        for j in range(l):
            sum1=sum1+(2**j)
        sum1=sum1+(n-l)
        return(str(sum1) +' '+ str(sum2))
    
    a=input().split()
    n=int(a[0])
    l=int(a[1])
    r=int(a[2])
    print(lost(n,l,r))