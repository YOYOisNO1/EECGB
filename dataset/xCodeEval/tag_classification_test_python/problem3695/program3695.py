def program3695():
    from collections import Counter,defaultdict
    I =lambda:int(input())
    M =lambda:map(int,input().split())
    LI=lambda:list(map(int,input().split()))
    n,k=M()
    a=LI()
    b=sorted(a)
    c=[]
    for i in range(n):
        if b[i]<=k:
            d=a.index(b[i])
            a[d]=-1
            c.append(d+1);k-=b[i]
    print(len(c))
    print(*c)