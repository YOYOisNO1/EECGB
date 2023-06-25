def program522():
    n , m = map(int,input().split())
    
    
    s = [ input() for i in xrange(n)]
    
    
    ans = 0;
    nub = 0;
    for i in s:
        if not 'S' in i:
            ans+= m
            nub+=1
    for i in xrange(m):
        str = ""
        for j in xrange(n):
            str+= s[j][i]
        if not 'S' in str:
            ans+=n-nub
            
            
    print ans