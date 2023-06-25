def program7316():
    import sys
    range = xrange
    input = input
    
    n,x,y = [int(x) for x in input().split()]
    
    import _numpypy
    zero = _numpypy.multiarray.dtype('int64').type()
    
    x = x + zero
    y = y + zero
    
    DP = _numpypy.multiarray.zeros(n+1, dtype = 'int64')
    for i in range(1,n+1):
        DP[i] = min(DP[i-1] + x, DP[(i+1)//2] + y + (x if i&1 else zero))
    
    print(DP[n])