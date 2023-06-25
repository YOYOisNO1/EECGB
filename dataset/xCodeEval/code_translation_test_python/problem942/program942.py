def program942():
    x, y = map(int, input().split())
    
    while 1:
        # Ciel
        if x > 1:
            if y > 1:
                x -= 2
                y -= 2
            else:
                print("Hanako")
                break
        elif x == 1:
            if y > 11:
                x = 0
                y -= 12
            else:
                print("Hanako")
                break
        else:
            if y > 21:
                y -= 22
            else:
                print("Hanako")
                break
        # Hanako
        if y > 21:
            y -= 22
        elif y > 11:
            if x > 0:
                x -= 1
                y -= 12
            else:
                print("Ciel")
                break
        elif y > 1:
            if x > 1:
                x -= 2
                y -= 2
            else:
                print("Ciel")
                break
        else:
            print("Ciel")
            break
    
    