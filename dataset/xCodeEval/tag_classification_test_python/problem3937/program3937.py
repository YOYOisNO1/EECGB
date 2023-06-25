def program3937():
    a, b = map(int, input().split(' '))
    if a == 2 or a == 3:
        print("YES")
        quit()
    
    else:
        while b != 0:
            if b%a == 0:
                b //= a
    
            elif b%a == 1:
                b -= 1
                b //= a
    
            elif b%a == a-1:
                b += 1
                b //= a
    
            else:
                print("NO")
                quit()
    
    print("YES")