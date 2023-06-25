def program3942():
    numbers = list(map(int, input().split()))
    
    w = numbers[0]
    m = numbers[1]
    
    no = False
    
    if w <= 3:
        m = 0
    
    while m:
        x = m % w
        
        if x <= 1:
            m = m // w
        elif x == w - 1:
            m = m // w + 1
        else:
            no = True
            break
    
    if no is False:
        print('YES')
    else:
        print('NO')