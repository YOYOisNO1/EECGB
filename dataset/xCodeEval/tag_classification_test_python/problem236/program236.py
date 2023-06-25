def program236():
    import math
    import bisect
    n=int(input())
    a=[]
    for k in range(1,11):
        for j in range((2**k)-1,-1,-1):    
            p=0
            l,m=0,0
            for i in range(k):
                y=j%2
                j//=2
                if y==0:
                    p+=((10**i)*4)
                    l+=1
                else:
                    p+=((10**i)*7)
                    m+=1
                
            if m==l:
                a.append(p)
    a.sort()
    print(a[bisect.bisect_left(a,n)])