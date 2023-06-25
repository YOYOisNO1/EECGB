    #!324.B
def modPow(n, po, mod):
        if po == 0:
            return 1;
        else:
            if po&1:
                return ( n * modPow(n,po-1,mod) ) % mod
            else:
                ret = modPow(n,po/2,mod) % mod
                return ( ret * ret ) % mod
    
    mod = int(1e9 + 7)
    
    n = int(input())
    ans = modPow(27,n,mod)
    mn = modPow(7,n,mod)
    if ans < mn:
        ans = ans + mod
    
    ans = ans - mn
    
    print(ans) % mod