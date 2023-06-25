def program1359():
    # coding: utf-8
    
    a = int(input())
    b = int(input())
    c = int(input())
    
    res = max(a+b*c, a+b+c, a*b+c, a*b*c, (a+b)*c, a*(b+c))
    
    print(res)