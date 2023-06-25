def program1239():
    import math
    
    
    guests = int(input())
    guests = guests+1
    
    if guests == 1:
        print("0")
    elif guests % 2 == 0:
        print(guests//2)
    
    else:
        print(guests)