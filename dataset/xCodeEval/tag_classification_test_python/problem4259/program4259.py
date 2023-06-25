def program4259():
    ﻿dic = {}
    l = map(int, input().split(" "))
    for i in l:
        dic[i] = l.count(i)
    has_four = False
    is_same = False
    for i in dic:
        if dic[i] >= 4:
            has_four = True
        if dic[i] == 6:
            has_four = True
            is_same = True
        elif dic[i] == 2:
            is_same = True
    
    if has_four and is_same:
        print("Elephant")
    elif has_four and not is_same:
        print("Bear")
    else :
        print("Alien")