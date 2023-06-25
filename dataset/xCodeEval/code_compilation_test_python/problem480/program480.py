def program480():
    st = input().split()
    a = {'0':int(st[1]),'1':int(st[2])
    st = input()
    coast = 0
    is_able = True
    for x in range(0,round(len(st)//2)):
        y = len(st) - x - 1
        if (y == x):
            if (st[x] == '2'):
                coast += min(a.values()) #если танцор в центре то выбираем для него самый дешевый костюм      
        else:
            if (st[x] == st[y]):
                if (st[x] == '2'):
                    coast += 2*min(a.values()) #если у двоих нет костюмов то выбираем для них два дешевых
            else:
                if (st[x] == '2'):
                    coast += a[st[y]] #выбиаем однаковые по соседям костюмы
                elif (st[y] == '2'):
                    coast += a[st[x]]
                else:
                    is_able = False #если сосдние костюмы изначально не совпаадют то прекращаем проверку
                    break
    
    if(is_able):
        print(coast)
    else:
        print(-1)