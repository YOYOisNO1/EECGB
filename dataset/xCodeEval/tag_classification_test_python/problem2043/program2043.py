def program2043():
    import sys
    if sys.subversion[0] == "PyPy":
        import io, atexit
        sys.stdout = io.BytesIO()
        atexit.register(lambda: sys.__stdout__.write(sys.stdout.getvalue()))
        
        sys.stdin = io.BytesIO(sys.stdin.read())
        input = lambda: sys.stdin.readline().rstrip()
    
    RS = input
    RI = lambda x=int: map(x,RS().split())
    RN = lambda x=int: x(RS())
    ''' ...................................................................... '''
    
    mod = 10**9+7
    
    n,k,d = RI()
    n += 1
    dp0,dp1 = [0]*n,[0]*n
    dp0[0] = 1
    
    for i in xrange(1,n):
        for j in xrange(1,min(i,k)+1):
            if j<d: dp0[i] += dp0[i-j]
            else: dp1[i] += dp0[i-j]
            dp1[i] += dp1[i-j]
            dp0[i] %= mod
            dp1[i] %= mod
            
    print(dp1[-1])
        
                
            
    
    
        
            
            
        
            
    
    
            