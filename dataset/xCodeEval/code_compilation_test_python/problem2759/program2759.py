def program2759():
    this = input()
    n = int(input())
    x,y = this[0], this[1]
    array = []
    for _ in range(n):
        array.append(input())
    f1, f2 = False, False
    for i in string:
        if f1 == False:
            if i[0] == x or i[-1] == x:
                f1= True
        if f2 == False:
            if i[-1] == y or i[0] == y:
                f2 = True
        if f1 == True and f2 == True:
            break
    f1 == False or f2 == False:
        print('NO')
    else:
        print('YES')