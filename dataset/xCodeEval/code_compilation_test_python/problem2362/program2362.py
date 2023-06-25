    dp=[]
    for i in xrange(333):
        tmp = []
        for j in xrange(333):
            tmp.append(-1)
        dp.append(tmp)
    
def win(a,b):
        if(dp[a][b]!=-1):return dp[a][b]
        if(a+b==0): return 0
        can = 0
        if a>0:
         for i in xrange(a):
            if(win(i,b)==0): can=1
        if(b>0 and can==0):
            for i in xrange(b):
                if(win(a,i)==0): can = 1
    
        if(min(a,b)>=1 and can==0):
         for i in xrange(min(a,b)):
            if(win(a-i-1,b-i-1)==0): can=1
        dp[a][b]=can
        return dp[a][b]
    
    n = map(int,input().split())[0]
    a = map(int,input().split())
    s1="BitLGM"
    s2="BitAryo"
    
    if n==2:
        if win(a[0],a[1])==1:
            print s1
        else: print s2
        exit(0)
    
    t = 0
    if n==1: t = a[0]
    else:
        t = (a[0]^a[1]^a[2])
    
    if(t>0):
        print s1
    else:
        print s2