def program3080():
    I=lambda:list(map(int,input().split()))
    n,=I()
    l=I()
    l.sort()
    ans=0
    i=0
    k=1
    while i<n:
     
        if l[i]<i//k:
            k+=1
        
        i+=1
    print(k)
        