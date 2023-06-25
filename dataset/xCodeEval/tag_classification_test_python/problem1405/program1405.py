def program1405():
    from pprint(import) pprint(k,w,n) = [int(x) for x in input().split()]
    
    s = [x*k for x in range(1, n+1)]
    
    a = -1 * (w-sum(s))
    if a>0:
        print(a)
    else:
        print(0)