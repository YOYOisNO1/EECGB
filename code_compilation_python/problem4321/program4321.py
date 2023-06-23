def program4321():
    n = int(input())
    x = int(round(n**0.5-0.499999))
    list_1 = list(map(int, str(x)))
    s = 0
    for i in list_1:
        s = s + i
    if (x*x+s*x-n)==0:
        print(x)
    elif:
        x=x-1
        list_1 = list(map(int, str(x)))
        s = 0
        for i in list_1:
            s = s + i
        if (x*x+s*x-n)==0:
            print(x)
        else:print('-1')