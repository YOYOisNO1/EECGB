    #---------------------------------------------
    import sys 
    # sys.stdin = open('input.txt', 'r'); sys.stdout = open('output.txt', 'w')
    mod = 1000000007
    get_arr = lambda: list(map(int, input().split()))
    get_int = lambda: int(input())
    get_ints = lambda: map(int, input().split())
    get_str = lambda: input()
    get_strs = lambda: input().split()
    #---------------------------------------------
    
def fn(n, k, d, flag, cache, mod):
        if(n==0 and flag): return 1
        if(n==0 and (not flag)): return 0
        if(n<0): return 0
    
        key = (n, flag)
        if key in cache: return cache[key]
    
        ans = 0
        for i in range(1, k+1):
            if(i>=d): ans += fn(n-i, k, d, True, cache, mod)
            else: ans += fn(n-i, k, d, flag, cache, mod)
            if(ans>=mod): ans %= mod
        cache[key] = ans
        return ans
    
    n, k, d = get_ints()
    print(fn(n, k, d, False, {}, mod))