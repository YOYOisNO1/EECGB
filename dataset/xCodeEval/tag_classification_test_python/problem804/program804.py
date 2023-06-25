def program804():
    #coding: utf-8
    
    point = [0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 15, 4]
    
    n = int(input())
    
    if n > 21 or n < 10:
        print(0)
    else:
        print(point[n - 10])