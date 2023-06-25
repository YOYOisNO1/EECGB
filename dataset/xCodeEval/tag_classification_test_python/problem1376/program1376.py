def nc2(a):
    	return (a*(a-1))/2
    f=list(map(int,input().split()))
    m=f[0]
    n=f[1]
    #print(m,n)
    mi=(int)(m/n)
    mir=m%n
    ma=(int)(max(mi,m-n+1))
    print((n-mir)*nc2(mi)+mir*nc2(mi+1),nc2(ma))