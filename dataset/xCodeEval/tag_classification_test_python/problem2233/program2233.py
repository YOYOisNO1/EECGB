    #map(int,input().split())
    
    a = int(input())
    
    p = map(int,input().split())
    
def memo(f):
        cache = {}
    def _f(*args):
            try:
                return cache[args]
            except KeyError:
                result = f(*args)
                cache[args] = result
                return result
            except TypeError:
                return f(*args)
        _f.cache = cache
        return _f
    
    @memo
def solve(ind=0):
        res = 0
        if ind >= len(p): return 1
        if p[ind] == 0:
            ind += 1
            while ind < len(p) and p[ind] == 0: ind+=1
            if ind == len(p): return 0
            res += solve(ind)
        else:
            res += solve(ind+1)
            ind += 1
            while ind < len(p) and p[ind] == 0:
                res += solve(ind+1)
                ind += 1
        return res
    
    print(solve())
        