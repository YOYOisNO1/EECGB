def program2342():
    n = int(input())
    a = list(map(int,input().split(' ')))
    mi = 360
    for i in range(1,n):
        a[i]=a[i-1]+a[i]
    
    for i in range(n):
        for j in range(i,n):
            sa = a[j]-(a[i-1] if i>0 else 0)
            sb = a[-1]-a[j]+(a[i-1] if i>0 else 0)#-(a[0] if i>1 else 0)
            if abs(sa-sb)<mi:
                mi = abs(sa-sb)
    ##        print(sa,' ',sb)
    print(mi)