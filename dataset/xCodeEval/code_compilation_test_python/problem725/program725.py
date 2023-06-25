def program725():
    n=int(input())
    tp=[]
    p=list(map(int,input().split()))
    ta=p.index(1)
    sa=p.index(n)
    tp.append(abs(ta-(n-1))
    tp.append(ta)
    tp.append(abs(sa-(n-1)))
    tp.append(sa)
    print(max(tp))