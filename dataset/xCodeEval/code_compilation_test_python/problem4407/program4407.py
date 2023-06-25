    a, b, h, w, n = map(int, input().split())
    extensions = map(int, input().split())
    extensions.sort(reverse=True)
    
    cache = {}
    
    
def fits(a, b, h, w):
        return all(i <= j for i, j in zip(sorted([a, b]), sorted([h, w])))
    
    
def compute(a, b, h, w, extensions):
        if fits(a, b, h, w):
            return 0
    
        if not extensions:
            return -1
    
        wider_count = run(a, b, h, w * extensions[0], extensions[1:])
        higher_count = run(a, b, h * extensions[0], w, extensions[1:])
    
        counts = [c for c in [wider_count, higher_count] if c != -1]
        if not counts:
            return -1
    
        return sorted(counts)[0] + 1
    
    
def run(a, b, h, w, extensions):
        cache_key = (w, h) + tuple(extensions)
        if cache_key not in cache:
            cache[cache_key] = compute(a, b, h, w, extensions)
        return cache[cache_key]
    
    
    print run(b, a, h, w, extensions)