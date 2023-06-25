def program809():
    a = int(input())
    
    if a < 11:
        print(0)
    elif a in range(11, 22):
        if a == 20:
            print(15)
        else:
            print(4)
    elif a in range(22, 26):
        print(0)