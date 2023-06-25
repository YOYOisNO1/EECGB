    M=1000000007
    n=input()
    f=[]
    f.append(1)
    for i in range(1,200000):
    	f.append((f[i-1]*i)%M)
def power(a,b):
    	if b==0:
    		return 1
    	z=power(a,b/2)%M
    	if b%2==0:
    		return (z*z)%M
    	return (((z*z)%M)*a)%M
    k=n-1
    n=n+k
    a=f[n]
    b=f[k]
    c=f[n-k]
    b=power(b,M-2)%M
    c=power(c,M-2)%M
    ans=(((a*b)%M)*c)%M
    print((ans*2-k-1+M)%M)