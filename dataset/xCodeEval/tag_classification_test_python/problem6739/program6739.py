def program6739():
    from fractions import gcd
    
    la, ra, ta = map(int, input().strip().split())
    lb, rb, tb = map(int, input().strip().split())
    
    if la < lb:
        la, lb = lb, la
        ra, rb = rb, ra
        ta, tb = tb, ta
    
    L1 = ra - la + 1
    L2 = rb - lb + 1
    
    g = gcd(ta, tb)
    
    d = (la - lb) % g
    ans1 = max(0, min(L1, L2 - d))
    
    d = (-d) % g
    ans2 = max(0, min(L2, L1 - d))
    
    ans = max(ans1, ans2)
    
    print(ans)