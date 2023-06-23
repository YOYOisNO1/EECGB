def program115():
    n=int(input())
    a=list(range(n))
    i=0
    while i<n:
        a[i]=int(input())
        i+=1
    c=list(range(n-1))
    i=1
    f=max(a)+1
    b=0
    while i<n-1:
        j=0
        while j<n-1:
            if j<i:
                c[j]=a[j]
            else:
                c[j]=a[j+1]
            j+=1
        j=0
        while j<n-2:
            if c[j+1]-c[j]>b:
                b=c[j+1]-c[j]
            j+=1
        if b<f:
            f=b
        b=0
        i+=1
    print(f)
    t=0