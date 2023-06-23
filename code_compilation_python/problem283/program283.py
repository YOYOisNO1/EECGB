def program283():
    n,k=map(int,input().split())
    a=[int(x) for x in input().split()]
    a.sort(reverse=True)
    x=a[:k]
    
    
    j=k
    while(j<n and a[j]==a[k-1]):
        x.append(a[j])
    c=0
    for i in x:
        if i==0:
            c+=1
    print(len(x)-c)