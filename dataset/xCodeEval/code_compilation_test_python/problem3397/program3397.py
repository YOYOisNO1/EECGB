def program3397():
    # -*- coding: utf-8 -*-
    
    width = int(input())
    height = int(input())
    x = int(input())
    y = int(input())
    
    n = x
    m = y
    
    while n != 0 and m != 0:
            if n > m:
                    n = n % m
            else:
                    m = m % n
    
    n += m
    x /= n
    y /= n
    
    w_new = 0
    h_new = 0
    bot = 1
    top = 2e9
    
    while (bot <= top):
            c = int((bot + top) / 2)
            if c * x <= width and c * y <= height:
                    bot = c + 1
                    w_new = c * x
                    h_new = c * y
            else:
                    top = c - 1
    
    print(w_new)
    print(" ")
    print(h_new)
    