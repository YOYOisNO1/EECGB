def program958():
    T,S,q=map(float, input().split())
    r=(q-1)/q
    n=0
    p=T-S
    while T>=1:
        n+=1
        i=S/(1-r)
        T-=i
        S=i
    print n