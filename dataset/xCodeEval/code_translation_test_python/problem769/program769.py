def program769():
    n=input()
    l=len(n)
    s=0
    for i,j in enumerate(n):
        if j=='A':
            p1=n.count('Q',0,i)
            p2=n.count('Q',i+1,l)
            p=p1*p2
            s+=p
    print(s)
        