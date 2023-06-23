def f(l,c,n):
        if l==2**(n-1):
            e = c[n-1]
        else:
            e = 0
        for i in range(n - 1):
            if l % 2 == 1:
                e += c[i]
            l /= 2
        return e
    n,l = map(int,input().split())
    c = map(int,input().split())
    for i in range(n):
        c[i]=min(c[j] for j in range(i,n))
    for i in range(n-1,-1,-1):
        c[i]=min(c[j]*(2**(i-j)) for j in range(0,i+1))
    w = (l / (2 ** (n - 1))) * c[n - 1]
    l %= (2 ** (n - 1))
    print w+min(f(i,c,n) for i in range(l,2**(n-1)+1))