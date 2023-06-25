def program364():
    
    x=input().split()
    n=int(x[0])
    k=int(x[1])
    c=0
    y=input().split()
    for i in range(n):
        y[i]=int(y[i])
    for j in range(n):
        if y[j]<=k:
            c+=1
        else:
            w=j
            break
    q=n-1
    while q>w:
        if y[q]<=k:
            c+=1
            q-+1
        else:
            break
    print(c)