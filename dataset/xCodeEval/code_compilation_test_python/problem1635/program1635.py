def program1635():
    __author__ = 'MatFuck'
    
    import sys
    
    #sys.stdin = open("1.txt")
    
    n = input()
    a = [int(x) for x in input().split()]
    p = [[0, 0] for i in range(n - 1)]
    
    for id in range(n - 1):
        p[id][0] = min(a [id], a [id + 1])
        p[id][1] = max(a [id], a [id + 1])
    
    
    p = sorted(p, key = lambda ps:(ps[0],ps[1]), reverse = False)
    
    ans = 0
    #print p
    
    for id_a, it_a in enumerate(p):
        for id_b, it_b in enumerate(p[id_a + 1:]):
            if (it_a[1] <= it_b[0]):
                break
            else:
            if (it_a[1] < it_b[1]) and (it_a[0] < it_b[0]):
                print "yes"
                sys.exit(0)
    
    
    
    print "no"