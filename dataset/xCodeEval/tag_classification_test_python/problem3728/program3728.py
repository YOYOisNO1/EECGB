def program3728():
    import sys,re,math
    f = sys.stdin
    
    #f = open('Carrot_Cakes.txt')
    n, t, k, d = [int(i) for i in f.readline().rstrip('\n').split()]
    b1 = 1 + (n - 1) / k
    time1 = b1 * t
    time2 = 10000
    if d < time1:
        b3 = 1 + (d - 1) / t
        ost = n - b3 * k
        if ost > k:
            ost1 = ost / 2
            ost2 = ost - ost1
        else:
            ost1 = 0
            ost2 = k
    
        b4 = 1 + (ost1 - 1) / k
        b5 = 1 + (ost2 - 1) / k
    
        time2 = d + b5 * t
    print("YES") if time1 > time2 else "NO"
    #f.close()