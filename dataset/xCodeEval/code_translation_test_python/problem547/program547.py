def program547():
    n,m = map(int,input().strip().split())
    a=map(int,input().strip().split())
    a.sort()
    #print(a)
    i=0
    small=a[n-1]-a[0]
    while(i+n<=m):
        if a[n+i-1]-a[i]<small:
            small=a[n+i-1]-a[i]
    
        i+=1
     #   print(small)
    print(small)