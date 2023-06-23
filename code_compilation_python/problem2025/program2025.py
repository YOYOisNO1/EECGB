def program2025():
    n, l, r = str(input()).split(" ")
    
        arr1 = []
        arr2 = []
    
        n = int(n)
        l = int(l)
        r = int(r)
    
        somma1 = 0
        somma2 = 0
    
        v = n - (l - 1)
        val = 1
    
        for j in range(v):
            arr1.append(1)
            somma1 += 1
    
        for i in range(l - 1):
            val *= 2
            somma1 += val
            arr1.append(val)
    
        v = n - (r - 1)
        val = 1
    
        for j in range(r - 1):
            somma2 += val
            arr2.append(val)
            val *= 2
    
        for i in range(v):
            arr2.append(val)
            somma2 += val
    
        print somma1, somma2