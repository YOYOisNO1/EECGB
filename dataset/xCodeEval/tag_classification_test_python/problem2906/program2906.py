def program2906():
    lamp = input()
    count = 0
    urai = 0
    w1,w2,w3,w4 = "","","",""
    d1,d2,d3,d4 = 0,0,0,0
    while urai < len(lamp):
        count += 1
        if lamp[urai] != "!":
            if count == 1:
                w1 = lamp[urai]
            elif count == 2:
                w2 = lamp[urai]
            elif count == 3:
                w3 = lamp[urai]
            elif count == 4:
                w4 = lamp[urai]
        else:
            if count == 1:
                d1 += 1
            elif count == 2:
                d2 += 1
            elif count == 3:
                d3 += 1
            elif count == 4:
                d4 += 1
        if count == 4:
            count = 0
        urai += 1
    
    if w1 == "R":
        if w2 == "B":
            if w3 == "Y":
                print(d1,d2,d3,d4)
            elif w3 == "G":
                print(d1,d2,d4,d3)
        elif w2 == "Y":
            if w3 == "G":
                print(d1,d4,d2,d3)
            elif w3 == "B":
                print(d1,d3,d2,d4)
        elif w2 == "G":
            if w3 == "Y":
                print(d1,d4,d3,d2)
            elif w3 == "B":
                print(d1,d3,d4,d2)
    elif w2 == "R":
        if w1 == "B":
            if w3 == "G":
                print(d2,d1,d4,d3)
            elif w3 == "Y":
                print(d2,d1,d3,d4)
        elif w1 == "Y":
            if w3 == "G":
                print(d2,d4,d1,d3)
            elif w3 == "B":
                print(d2,d3,d1,d4)
        elif w1 == "G":
            if w3 == "Y":
                print(d2,d4,d3,d1)
            elif w3 == "B":
                print(d2,d3,d4,d1)
    elif w3 == "R":
        if w1 == "Y":
            if w2 == "G":
                print(d3,d4,d2,d1)
            elif w2 == "B":
                print(d3,d2,d1,d4)
        elif w1 == "G":
            if w2 == "Y":
                print(d3,d4,d2,d1)
            elif w2 == "B":
                print(d3,d2,d4,d1)
        elif w1 == "B":
            if w2 == "Y":
                print(d3,d1,d2,d4)
            elif w2 == "G":
                print(d3,d1,d4,d2)
    elif w4 == "R":
        if w1 == "Y":
            if w2 == "G":
                print(d4,d3,d1,d2)
            elif w2 == "B":
                print(d4,d2,d1,d3)
        elif w1 == "G":
            if w2 == "Y":
                print(d4,d3,d2,d1)
            elif w2 == "B":
                print(d4,d2,d3,d1)
        elif w1 == "B":
            if w2 == "Y":
                print(d4,d1,d2,d3)
            elif w2 == "G":
                print(d4,d1,d3,d2)