def program1939():
    a1, b1 = map(int, input().split())
    if a1 == 9 and b1 == 1:
            print(999, 1000)    
    elif a1 - b1 > 1:
        print(-1) 
    elif b1 - a1 > 1:
        print(-1)
    else:
        if a1 == b1:
            print(a1*100 + 12, b1 * 100 + 13)
        elif a1 < b1:
            print(a1*100 + 99, b1 * 100)
        elif a1 > b1:
            print(-1)