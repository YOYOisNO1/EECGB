def program1585():
    n,m=list(map(int,input().split()))
    if m<=n:
        print(n-m)
    c=0
    else:
        while m>n:
            if m%2:
                m=m+1
            else:
                m=m//2
            c=c+1
        c=c+(n-m)
        print(c) 