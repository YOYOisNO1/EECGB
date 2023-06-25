def program2028():
    import sys
    from random import randint
    from time import time
    
    line=map(lambda x:int(x),sys.stdin.readline().strip('\n').split(" "))
    n=line[0]
    k=line[1]
    d=line[2]
    
    numd=[]
    num=[1]
    for i in xrange(1,k):
        num.append(sum(num[0:i])%1000000007)
        #num.append(num[-1]*2%100000007)
    for i in xrange(0,d):
        numd.append(0)
    for i in xrange(d,k):
        #print(i,numd,num)
        numd.append((sum(numd[i-d+1:i])+sum(num[0:i-d+1]))%1000000007)
    
    
    #print(numd,num)
    for i in xrange(k,n+1):
        numd.append(0)
        for j in xrange(1,d):
            numd[i]=(numd[i]+numd[i-j])%1000000007
        for j in xrange(d,k+1):
            numd[i]=(numd[i]+num[i-j])%1000000007
        num.append(0)
        for j in xrange(1,k+1):
            num[i]=(num[i]+num[i-j])%1000000007
    #print(numd,num)
    print(numd[n]%1000000007)