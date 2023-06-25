def program2254():
    n=int(input())
    a=[int(i) for i in input().split()]
    a.sort()
    i=0
    k=0
    while i<=n and a[i]==0:
        i+=1
    else:
        while i<n:
            if a[i]!=a[i-1]:
                k+=1
            i += 1
    
    if k==0:
        print(k+1)
    else:
        print(k)