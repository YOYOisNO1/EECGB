    
def p(b,e):
    
        ans = 1
    
        while e > 0 :
            if e % 2 :
                ans = (ans * b) % MOD  
            b = ( b * b ) % MOD
            e = (e >> 1) % MOD
    
        return ans 
    
    MOD = 1000000007
    n = input()
    
    # base = p(2,int(n))
    if n == 0:
        print "1"
    else :
        ans = 2*pow(4,int(n) - 1,MOD) + pow(2,int(n) - 1,MOD)
        # ans = (int(base)/2) % MOD 
        # base = base % MOD
        # ans = (ans * (base + 1) ) 
        print ans % MOD
            