def program2663():
    n,d=input().split()
    n,d=[int(n),int(d)]
    c=0
    a=[int(i) for i in input().split()]
    x=a[n-1]-a[0]
    #print(a)
    while x>d::
        #print(a)
        del a[n-1]
        n=n-1
        c+=1
        x=a[n-1]-a[0]
    print(c)