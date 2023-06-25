def program2271():
    k,l,m,n,d=[int(input()) for i in range(5)]
    xs=[x for x in range(d)]
    s=set()
    for i in (k,l,m,n):
        s.update([xs[i*a-1] for a in range(1,d//i+1)])
    print(len(s))