def program503():
    p, q, x = map(int,input().split())
    
    if x == 1 :
        print('0' * p, end = '')
        print('1' * q, end = '')
        
    else :
        if p > q :
            l = '0'
            h = '1'
            a = p - 1
            b = q - 1
        else :
            h = '0'
            l = '1'
            a = q - 1 
            b = p - 1
        print(l, end = '')
        print(h, end = '')
        flag = -1
        x -= 1
    
        while x > 1 :
            if a > 0 :
                print(l, end = '')
                x -= 1
                a -= 1
                flag = 0
            if b > 0 and x != 1:
                print(h, end = '')
                x -= 1
                b -= 1
                flag = 1
        if flag == 0 :
            print(l * a, end = '')
            print(h * b, end = '')
        
        else :
            print(h * b, end = '')
            print(l * a, end = '')
        