def program2114():
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[0]*n
    for i in range(0,n):
        b[i]=a[i]
    m=0
    p=0
    for i in range(0,n):
        p=p+b[i]
        for j in range(i+1,n):
            z=0
            for k in range(i,j+1):
                a[k]=1-b[k]
                z=z+a[k]
            for x in range(0,i):
                z=z+b[x]
            for x in range(j+1,n):
                z=z+b[x]
            if z>=m:
                m=z
    if p==0:
        print(n)
    elif p==n
        print(n-1)
    else:
        print(m)
            