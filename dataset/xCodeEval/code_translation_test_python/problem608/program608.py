def program608():
    ch="chest"
    bi="biceps"
    ba="back"
    m={ch:0,bi:0,ba:0}
    n=int(input())
    a=map(int,input().split())
    s=[ch,bi,ba]*n
    z=zip(s[:n],a)
    for e,ai in z:
        m[e]+=ai
    print(max(m,key=m.get))
    
    
    