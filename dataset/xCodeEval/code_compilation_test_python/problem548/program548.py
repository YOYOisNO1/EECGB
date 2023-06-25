def program548():
    n = input().split(' ')
    day = int(n[0])
    ident = n[2]
    
    elif ident == "week":
        if day > 6:
            print(51)
        else:
            print(52)
    else:
        if day <30:
            print(12)
        elif day == 30:
            print(11)
        else:
            print(7)