def program2989():
    n=int(input())
    lis=map(int,input().split())
    lis=sorted(lis)
    d1,d2=0,0
    for i in xrange(n/2):
        d1+=abs(2*i+1-lis[i])
        d2+=abs(2*i+2-lis[i])
    print min(d1,d2