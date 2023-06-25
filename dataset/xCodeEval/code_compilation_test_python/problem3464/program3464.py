def list_fact(n):
        F=[0]*(n+1)
        F[0]=1
        for i in range(1,n+1):
            F[i]=i*F[i-1]
        return F
    S=str(input())
    l=list(map(int, S.split(' ')))
    n,m=l[0],l[1]
    F=list_fact(n*m)
    S=0
    for k in range(1,min(n,m)+1):
        S+=k*F[m]*F[n]*F[(n-1)*m]*F[(m-1)*n]/(n*F[n*m]*F[k-1]*F[n-k]*F[m-k]*F[n*m-n-m+k])
    print(S)