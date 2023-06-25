def program6203():
    r1 , c1 , r2 , c2 = map(int , input().split())
    
    a , b , c = 0 , 0 , 0
    
    if r1 == r2 or c1 == c2:
        a = 1
    else:
        a = 2
    
    if abs(r1 - r2) == abs(c1 - c2):
        b = 1
    elif (r1 + r2 + c1 + c2) % 2 == 0:
        b = 2
    else:
        b = 0
    
    c = max (abs(r1 - r2) , abs(c1 - c2))
    
    print(a) , b , c