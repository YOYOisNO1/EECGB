def check(m):
        moneyrq = 0
        if rqb>0: moneyrq += max(0,(m*rqb-nb)*pb)
        if rqs>0: moneyrq += max(0,(m*rqs-ns)*ps)
        if rqc>0: moneyrq += max(0,(m*rqc-nc)*pc)
        return moneyrq<=have
    
    R = lambda: list(map(int,input().split()))
    s = input()
    rqb,rqs,rqc = s.count('B'),s.count('S'),s.count('C')
    nb,ns,nc = R()
    pb,ps,pc = R()
    have = int(input())
    lo,hi = 0,int(1e18)
    while lo<hi:
        m = (lo+hi)//2
        if check(m): lo = m+1
        else: hi = m
    if not check(lo): lo -= 1
    print(lo)