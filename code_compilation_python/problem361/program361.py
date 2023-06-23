def program361():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    i=0
    j=n-1
    c=0
    while(i < j):
        if a[i] <=k and a[j] > k:
            c+=1
            i+=1
        elif a[j] <= k and a[i] > k:
            c+=1
            j-=1
    print(c)