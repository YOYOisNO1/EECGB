def program2237():
    n = input()
    c = map(int, input().split())
    
    total = 1
    
    if 1 not in c :
        print(0)
        exit()
    
    i = c.index(1)
    
    while True :
        c[i] = -1
        if 1 in c :
            j = c.index(1)
            total = total * (j-i)   
            i = j
        else :
            break
    
    print(total)