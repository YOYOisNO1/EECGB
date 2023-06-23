    import math
    import sys
    
    k, pa, pb = list( map( int, input().split() ) )
    
    memo = {}
    
    sys.setrecursionlimit(1500*1500*2)
    
    MOD = (10**9 + 7 )
    
def pow( a, b ):
    
        ret = 1
    
        while b > 0:
    
            if b & 1:
                ret = (ret*a)%MOD
    
            a = (a*a)%MOD
    
            b //= 2
    
        return ( ret )
    
def inv(a):
       return pow( a, MOD-2 )
    
def f( total_a, total_ab ):
    
        if total_a+total_ab >= k:
            return total_a+total_ab + pa * inv(pb)
    
        if (total_a,total_ab) in memo:
            return memo[ (total_a,total_ab) ]
    
        Best = 0
    
        Best += pa * f( total_a+1, total_ab ) * inv( pa + pb )
        Best %= MOD
    
        Best += pb * f( total_a, total_a+total_ab ) * inv( pa + pb )
        Best %= MOD
    
        memo[ (total_a,total_ab) ] = Best
    
        return ( Best )
    
    #print( k, pa, pb )
    
    print( ( f(1,0) ) % MOD )