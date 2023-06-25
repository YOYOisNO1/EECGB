def func(r, k, a) :
        out = 0
        if r <= k:
            out = 2**(r-1)
        else : 
            
            for i in range(1,k+1) :
                if i <= r :
                    if a[r-i] != -1 :
                        out = out + a[r-i]
                    else:
                        out = out + func(r-i, k, a)
                else :
                    break;
        a[r] = out
        return out
            
    n,k,d = map(int, input().split())
    x = [-1]*(n+1)
    y = [-1]*(n+1)
    print((func(n,k,x)) - func(n, d-1,y)) % 1000000007   