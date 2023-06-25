def program529():
    n, x = map(int, input().split())
    v = [int(i) for i in input().split()]
    
    cont = [0] * 200
    
    for i in v:
        cont[i] += 1
        
    res = 0
    for i in range(x):
        if cont[i] == 0:
            res += 1
            
    if cont[x] == 1:
        res += 1
        
    print(res)