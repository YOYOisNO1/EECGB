def program738():
    n=int(input())
    if n==10**9
        ans=1
    else:
        ans=0
    for i in xrange(8,-1,-1):
        if n>=(10**i):
            ans+=(n-(10**i)+1)*(i+1)
            n=(10**i)-1
    print ans