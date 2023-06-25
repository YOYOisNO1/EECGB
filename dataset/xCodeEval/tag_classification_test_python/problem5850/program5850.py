def program5850():
    s=input()
    a=[]
    for j in range(1,len(s)):
        a.append(int(s[j]))
    
    k=[[] for j in range(10)]
    m=0
    for j in range(10):
        c=[0]*(10)
        c[j]=1
    
        r=0
        while(r<len(a)):
            p=0
            d = [0] * (10)
            while(p<10):
    
                if (p+a[r])%2==0:
                    q=(p+a[r])//2
                    d[q]+=c[p]
                    d[p]+=-c[p]
                else:
                    q = (p + a[r]) // 2
                    u=q+1
                    d[q] += c[p]
                    d[u]+=c[p]
                    d[p]+=-c[p]
    
    
                p+=1
            for i in range(10):
                c[i] += d[i]
    
    
    
            r+=1
    
        m+=sum(c)
    
    
    j=int(s[0])
    f=0
    q=0
    while(q<len(a)):
        if (j+a[q])%2==0:
            if a[q]!=(j+a[q])//2:
                f=1
                break
        else:
            e=(j + a[q])// 2
            if a[q]!=e and a[q]!=(e+1):
                f=1
                break
        j=a[q]
        q+=1
    if f==0:
        m+=-1
    print(m)
    
    
    
    
    