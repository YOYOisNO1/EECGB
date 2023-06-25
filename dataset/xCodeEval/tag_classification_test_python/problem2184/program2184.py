def program2184():
    a = int(input())
    i = 0
    
    if a % 2 == 1:
        while a != 1:
            x = 1
            lx = 1
            while a > x:
                lx = x
                x *= 2
            a = a - lx
            i += 1
        print(i + a)
    elif a % 2 == 0:
            while a != 0:
                x = 1
                lx = 1
                while a >= x:
                    lx = x
                    x *= 2
                a = a - lx
                i += 1
            print(i)