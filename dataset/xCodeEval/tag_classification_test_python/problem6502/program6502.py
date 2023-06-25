def program6502():
    R = lambda: map(int,input().split())
    a,b = R()
    x,y,z = R()
    a -= x*2
    a -= y
    b -= y
    b -= z*3
    if a >= 0 and b >= 0:
        exit(print(0))
    if a >= 0 and b < 0: 
        exit(print(abs(b)))
    if a < 0 and b >= 0:
        exit(print(abs(a)))
    if a < 0 and b < 0:
        exit(print(abs(a + b)))
    print(0)
        
    
    