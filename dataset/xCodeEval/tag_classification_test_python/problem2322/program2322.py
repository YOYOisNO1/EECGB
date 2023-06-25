def s():
        n = input().split()
        r = int(n[0])
        b = int(n[1])
        k = l = m = 0
        if b > r:
            k = r
            l = b - r
        else:
            k = b
            l = r - b
        m =  l / 2
        print(k,') ',m
        
    s()