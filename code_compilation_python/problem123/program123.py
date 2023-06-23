def fn(n,a):
        c = 0
        for i in range(1,6):
            x = a+i-1
            if x%(n+1) == 0:
                continue
            else:
                c += 1
        return c
    
    
    
    n = int(input())
    
    a = int(input())
    
    print (fn(n,a))