def program4086():
    # always avoid floats (even in Python :( )
    
    n = input()
    lo, hi = 1, n
    
    while lo < hi:
        mid = lo + (hi - lo) / 2
    
        amt = n
        cnt = 0
        k = mid
        while amt > 0:
            vas = min(amt, k)
            amt -= vas
            cnt += vas
    
            pet = amt // 10
            amt -= pet
            
        if 2 * cnt >= n:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)