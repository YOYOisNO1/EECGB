def program4809():
    a = int(input())
    b = int(a**(1/2))**2
    if (b - a) == 0:
        print(int(4*(b**(1/2))))
    elif (a - b) <= (b**(1/2)) and (b-a) != 0:
        print(int(4*(b**(1/2))+2))
    else:
        print(int(4*((b**(1/2))+1)))