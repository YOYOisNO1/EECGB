def program1003():
    
    x,y = list (map (int, input().split()))
    a = y*10 - 1 
    b = y * 10
    c = y * 10 + 1 
    
    if x - y == 8:
        print(a,b)
    elif x > y && x - y != 8:
        print(-1)
    elif y - x >= 2:
        print(-1)
    elif y == x:
        print(b,c)
    elif y - x == 1:
        print(a,b)
    
    
    
    