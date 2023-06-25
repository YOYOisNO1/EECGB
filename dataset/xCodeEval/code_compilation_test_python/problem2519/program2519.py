def program2519():
    import math
    
    line = input()
    a, b = [int(x) for x in line.split()]
    
    nice = 0
    
    for i in range (1, a+1):
        for j in range (1, b):
            nice += (i*j)*b + j
        
    print nice%1000000007