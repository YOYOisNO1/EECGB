def program3233():
    from math import log
    n,l = map(int,input().split())
    c = map(int,input().split())
    for i in range(n):
        c[i]=min(c[j] for j in range(i,n))
    for i in range(n-1,-1,-1):
        c[i]=min(c[j]*(2**(i-j)) for j in range(0,i+1))
    s=[(l/(2**i))*(2**i)+2**(i-1) for i in range(1,int(log(l,2))+3)]
    i = 0
    while i<len(s):
        if s[i]<l:
            s.remove(s[i])
        else:
            i += 1
    x = []
    for i in s:
        w = i/(2**(n-1))*c[n-1]
        i = i%(2**(n-1))
        for j in range(n-1):
            if (i/(2**j))%2==1:
                w += c[j]
        x.append(w)
    print(min(x))