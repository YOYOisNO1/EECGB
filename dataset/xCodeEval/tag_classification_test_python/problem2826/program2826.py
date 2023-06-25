def program2826():
    I=lambda:list(map(int,input().split()))
    q=I()
    w=I()
    e=I()
    print(['NO','YES'][any(a+c<=x and y>=max(b,d)for x,y in(q,q[::-1])for a,b in(w,w[::-1])for c,d in(e,e[::-1]))])