    import os
    
    
def main():
        _n, _k, _g = os.read(0, os.fstat(0).st_size).split()
    
        n, k = int(_n), int(_k)
        g = [x - 65 for x in _g]
    
        e = [-1] * 26
        for i in range(n):
            e[g[i]] = i
        curS = 0
        f = 1
        met = [0] * 26
        for i in range(n):
            if not met[g[i]]:
                curS += 1
                met[g[i]] = 1
            if curS > k:
                f = 0
                break
            if i == e[g[i]]:
                curS -= 1
    
        print('NO' if f else 'YES')
    
    
    main()