def program3895():
    n=int(input())
    l=list(map(int,input().split()))
    
    l=sorted(l)
    p=l[n-1]
    k=l[n-1]
    
    for i in range(n-2,-1,-1) :
        if l[i]>=p :
            if p==0 :
                p=1
            k=k+p-1
            p=p-1
        else :
            p=l[i]
            k=k+l[i]
    print(k)