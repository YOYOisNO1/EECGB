def program5604():
    a,b = sorted(map(int,input().split()))
    t1 = a*(b/2)+(a/2+a%2)*(b%2)
    if a==2:
        t1 = max(t1,a*(2*(b/4)+min(b%4,2)))
    if a==1: t1=b
    print(t1)