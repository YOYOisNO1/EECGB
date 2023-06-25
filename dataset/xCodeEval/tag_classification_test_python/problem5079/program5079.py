def program5079():
    n,a,b,c,d= map(int,input().split())
    l=[a+b,a+c,b+d,c+d]
    print((n*max(0,(n-max(l)+min(l)))))