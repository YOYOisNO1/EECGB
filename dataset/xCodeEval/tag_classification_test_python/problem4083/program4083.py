def program4083():
    days = int(input())
    
    if days % 7 == 0:
        print(days//7 * 2, days//7 * 2)
    elif days < 7:
        if days == 6:
            print(1, 2)
        elif days == 1:
            print(0, 1)
        elif days >= 2:
            print(0, 2)
    elif days % 7 == 1:
        print(days//7 * 2, days//7 * 2 + 1)
    elif days%7 == 6:
        print(days//7 * 2 + 1, days//7 * 2 + 2)
    elif days % 7 >= 2:
        print(days//7 * 2, days//7 * 2 + 2)