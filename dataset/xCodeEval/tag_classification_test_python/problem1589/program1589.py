def program1589():
    a, b = map(int, input().split())
    
    turn = True
    now = 1
    while True:
        if turn:
            if a < now:
                print("Vladik")
                exit()
            else:
                a -= now
        else:
            if b < now:
                print("Valera")
                exit()
            else:
                b -= now
        now += 1
        turn = not turn