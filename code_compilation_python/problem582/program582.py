def comb(n, r):
        if n == 0 or r == 0: return 1
        return comb(n, r - 1) * (n - r + 1) / r 
    n,m=map(int,input().split())
    if n/m==1:
        if n==m:
            print 0,0
        else:
            max=comb(n-m+1,2)
            print n%m,max
    a=[n/m]*m
    max=comb(n-m+1,2)
    else:
        for i in range(0,n%m):
            a[i]+=1
        if a[0]!=a[-1]:
            min=comb(a[0],2)*a.count(a[0])+comb(a[-1],2)*a.count(a[-1])
        elif a[0]==a[-1]:
            min=comb(a[0],2)*m
        print min,max