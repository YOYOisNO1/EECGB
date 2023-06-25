    from operator import __xor__
    
    known = {1:0, 2:0}
    win = {1:-1, 2:-1}
    
def split(stone, k):
        n = int( ( stone - (k*(k-1)/2)) / k)
        if n <= 0 or k*n + k*(k-1)/2 != stone:
            return []
        return range(n, n+k)
    
def mex(iterable):
        i = 0
        while i in iterable:
            i += 1
        return i
    
def g(stone):
        if stone in known:
            return known[stone]
        loc = set()
        win_k = -1
        for k in range(2, int((2*stone) ** .5) + 1):
            sp =  split(stone, k)
            if sp:
                xor = reduce(__xor__, map(g, sp), 0)
                loc.add(xor)
                if xor == 0 and win_k == -1:
                    win_k = k
        xor = mex(loc)
        known[stone] = xor
        win[stone] = win_k
        return xor
    
    if __name__ == "__main__":
        n = int(input().strip())
        for i in range(10**5): g(n)
        print win[n]