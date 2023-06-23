    from itertools import product
    from bisect import bisect_left as bsearch
    
    MAXDIG = 12
    
def main():
        global MAXDIG
        (l, r) = map(int, input().split(' '))
        luckies = []
        for i in range(MAXDIG):
            lst = product([7, 4], repeat = i)
            for x in lst:
                s = ''.join(map(str, x))
                if len(s) != 0:
                    num = int(s)
                    luckies.append(num)
        luckies = sorted(luckies)
        s = 0
        i = bsearch(luckies, l)
        for k in range(l, r + 1):
            if luckies[i] < k:
                i += 1
            s += luckies[i]
        print(s)
    
    
    main()
        
    
    