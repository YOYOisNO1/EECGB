def program852():
    x=map(int,input().split())
    k=x[1]
    n=x[0]
    if len(str(k))=<n:
        s=str(k)
        for i in range(n-1):
            s+=str(0)
        if k>=10:
            s=s[:-1]
    else:
        s=str(-1)
    print s