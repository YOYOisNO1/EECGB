    from scipy.special import binom, comb
def D(m,n):
        tmp=0
        for k in range(m+1):
            print('(m,k)=(%d, %d)='%(m,k),binom(m,k))
            print('(n+k, m)=(%d, %d)='%(n+k, m), binom(n+k,m))
            print('product=', binom(m,k)*binom(n+k,m))
            tmp+=binom(m,k)*binom(n+k,m)
        print(tmp)
        return tmp
def t(m,n,k):
        print('(m,k)(n+k,m)=', binom(m,k)*binom(n+k,m))
    
def prob(n,k):
        p1=binom(k,3)/binom(n,3)
        p2=binom(k,2)*(n-k)/binom(n,3)
        p3=1/2*k*binom(n-k,2)/binom(n,3)
        ptot=p1+p2+p3
        return ptot
    np=input()
    np=np.split(' ')
    n=int(np[0])
    p=float(np[1])
    left=0
    right=n
    while(left<right):
        k=(left+right)//2
        if(prob(n,k)<p):
            left=k+1
        else:
            right=k
    
    while(prob(n,k)<p):
        k+=1
    
    print(k)
            
        