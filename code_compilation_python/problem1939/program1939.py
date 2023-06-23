def program1939():
    k,n,w = map(int,input().split())
    a=k
    l=w*k
    s=w/2*(a+l)
    # print s,a,l
    if s-n>=0:
        print s-n
    else
        print 0