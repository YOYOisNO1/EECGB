def program1780():
    
    n, m = map(int, input().split())
    
    key = True
    total = m
    while key == True:
        for i in range(1, n+1):
            if total <= i:
                break
            total-=i
        if total <= 0:
            key = False
    
    print(total)
    
    
    
    
    
    