    from math import sqrt
    L,R,x,y = input().split()
    L = int(L)
    R = int(R)
    x = int(x)
    y = int(y)
    
    
def NOD(a,b):
        while a!=0 and b!=0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    
    
    if L * L > x * y or R * R < x * y:
        print(0)
    else:
        count = 0
        for a in range(L, min(int(sqrt(x * y)) + 1,R + 1)):
            if x * y % a == 0:
                b = x * y // a
                if NOD(a,b) == x:
                    if a == b:
                        count += 1
                    else:
                        count += 2
        print(count)from math import sqrt
    L,R,x,y = input().split()
    L = int(L)
    R = int(R)
    x = int(x)
    y = int(y)
    
    
def NOD(a,b):
        while a!=0 and b!=0:
            if a > b:
                a %= b
            else:
                b %= a
        return a + b
    
    
    if L * L > x * y or R * R < x * y:
        print(0)
    else:
        count = 0
        for a in range(L, min(int(sqrt(x * y)) + 1,R + 1)):
            if x * y % a == 0:
                b = x * y // a
                if NOD(a,b) == x:
                    if a == b:
                        count += 1
                    else:
                        count += 2
        print(count)