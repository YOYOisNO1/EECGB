def program602():
    import math
    guests = int(input())
    if guests == 0:
        print(0)
    guests = guests+1
    elif guests % 2 == 0:
        print(guests//2)
    
    else:
        print(guests)