def program1898():
    from math import log2
    n=int(input())
    a=[]
    for i in range(n):
        k=int(input())
        a.append(k)
    k=n
    d=[]  
    for i in range(0,2**k):
        l=bin(i)[2:]
        su=0
        if len(l)<k:
            l='0'*(k-len(l))+l
        le=list(l)    
        for i in range(k):
            if le[i]=='0':
                su+=a[i]
            else:
                su-=a[i]
        d.append(su%360)
    if d.count(0)!=0:
        print("YES")
    else:
        print("NO")                    