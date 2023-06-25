def kil(n):
        if n<8: return (n,n)
        m=int(n**(1/3))
        k1,v1=kil(n-m*m*m)
        k2,v2=kil(m*m*m-1-(m-1)*(m-1)*(m-1))
        return (k1+1,v1+m*m*m) if (k1,v1+m*m*m)>(k2,v2+(m-1)*(m-1)*(m-1)) else (k2+1,v2+(m-1)*(m-1)*(m-1))
      
    n=int(input())
    print(*kil(n))