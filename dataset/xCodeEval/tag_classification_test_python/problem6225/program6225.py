def program6225():
    import math
    
    DASHA = 'Dasha'
    MASHA = 'Masha'
    EQUAL = 'Equal'
    
    a, b = map(int, input().strip().split())
    g = math.gcd(a, b)
    a //= g
    b //= g
    
    if abs(a - b) == 1:
    	print(EQUAL)
    elif (a < b):
    	print(DASHA)
    else:
    	print(MASHA)
    