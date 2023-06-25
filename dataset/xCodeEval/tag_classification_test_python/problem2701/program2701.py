def fn(A, B, i, n, cuts, o, e, cache):
        if(i>=n-1 and B>=0): return cuts
        if(B==0): return cuts
        if(B<0): return 0
        
        key = (B, i, cuts, o, e)
        ans = -1
        if key in cache:
            ans = cache[key]
        else:
        
            if(A[i]%2==0): e += 1
            else: o += 1
            
            if(o==e and o!=0 and e!=0):
                cache[key] = max(fn(A, B-abs(A[i]-A[i+1]), i+1, n, cuts+1, o, e, cache), fn(A, B, i+1, n, cuts, o, e, cache))
            else:
                cache[key] = fn(A, B, i+1, n, cuts, o, e, cache)
            ans = cache[key]
        return ans
    
    n, B = map(int, input().split())
    A = map(int, input().split())
    print(fn(A,) B, 0, n, 0, 0, 0, {})