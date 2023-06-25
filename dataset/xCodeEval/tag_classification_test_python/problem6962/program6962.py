def prob(db, n):
        return db*(db-1)*(db-2)+(n-db)*db*(db-1)*3+(n-db)*(n-db-1)*db*3/2
    
    n, p = input().split()
    n = int(n)
    p = float(p)
    p *= n*(n-1)*(n-2)
    
    
    s = 0
    e = n-1
    while s <= e:
        act = (s+e)//2
        if e-s == 1:
            if prob(s, n) >= p:
                break
            else:
                s = e
                break
        else:
            if prob(act, n) >= p:
                e = act
            else:
                s = act
    
            
    print(s)
        