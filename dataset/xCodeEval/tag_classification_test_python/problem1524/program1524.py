def program1524():
    import bisect
    n,m,k=list(map(int,input().split()))
    l=[0]+list(map(int,input().split()))
    l.sort()
    s=sum(l)-n
    
    c=0
    if m-s>k:
        print(-1)
    else:
        s=0
        for i in range(k):
            s=s+l[len(l)-1-i]
        if m-s>0:
            c=0
            
            k=k-1
            i=len(l)-1
            while m-1>k:
                m=m-l[i]+1
                i=i-1
                c=c+1
            
            print(c)
        else:
            i=len(l)-1
            while m>k and k>0: 
                
                m=m-l[i]
                k=k-1
                c=c+1
                i=i-1
                
            print(c)