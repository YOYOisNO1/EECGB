def program2369():
    n,m=map(int,input().split())
    a=[0 for i in range(n+1)]
    b=[0 for i in range(n+1)]
    c=[0 for i in range(n+1)]
    
    k=input().split()
    sum=0
    sum1=0
    for i in range(n):
        a[i]=int(k[i])
        sum1=sum1+a[i]
        sum=sum+a[i]-(a[i]/2)
    for i in range(n):
        for j in range(n):
            if a[i]<a[j]: c[i]+=1
    
    if m<sum:
        print(-1)
    else:
        if m==sum:
            print(" ").join(str(a[i]-a[i]/2) for i in range(n))
        else:
            max=0
            for i in range(0,n):
                if a[i]>a[max]: max=i
                b[i]=a[i]-a[i]/2
                m=m-b[i]
            for i in range(n):
                for pointer in range(n):
                    if c[pointer]==i:
                        if a[pointer]-b[pointer]<m:
                            m = m + b[pointer] - a[pointer]
                            b[pointer]=a[pointer]
    
                        if a[pointer]-b[pointer]>=m:
                           b[pointer]=b[pointer]+m
                           m=0
            print(" ").join(str(b[i]) for i in range(n))