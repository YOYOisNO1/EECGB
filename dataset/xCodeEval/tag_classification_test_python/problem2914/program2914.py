def program2914():
    from math import sqrt
    n = int(input())
    
    if n == 1:
        print(1)
    else:
        d = [1]
        i, p = 2, n
        while p > 1 and i * i <= p:
            if p % i == 0:
                d.append(i)
                while p % i == 0:
                    p //= i
    
            i += 1
    
        if p > 1:
            d.append(p)
    
        #print(d)
    
        if len(d) == 2:
            print(d[1])
        else:
            print(1)