def program4656():
    n,k=map(int,input().split())
    l=set()
    d=dict()
    s=input()
    f='NO'
    for i in range(n):
        d[s[i]]=i
    for i in range(n):
        l.add(s[i])
        if(len(l)>k):
            f='YES'
            break
        if(d[s[i]]==i):
            l.remove(s[i])
    print(f)