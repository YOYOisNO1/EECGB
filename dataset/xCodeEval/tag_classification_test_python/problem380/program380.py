def program380():
    import math
    
    a= str(input())
    c= a.count('a')
    n= len(a)-c
    l= math.ceil(len(a)/2)
    if c>n:
        print(len(a))
    else:
        print(2*c-1)