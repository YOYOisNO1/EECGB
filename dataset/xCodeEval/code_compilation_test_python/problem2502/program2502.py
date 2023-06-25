def program2502():
    inp = input()
    firstGroup, c = inp.split('=')
    a, b = firstGroup.split('+')
    
    A = len(a)
    B = len(b)
    C = len(c)
    
    elements = [A, B, C]
    maxVal = max([A, B, C])
    impo = True
    firstExp = A+B
    
    if firstExp == C:
        print(inp)
        impo = False
    else:
        i = 0
        while i <= 2:
            item = elements[i]
            exi = elements[:i]+elements[i+1:]
            if (exi[0]+1+exi[1]) == (item-1):
                print(("|"*(exi[0]+1)) + "+" +("|"*exi[1]) + "=" + ("|"*(item-1)))
                impo = False
            else:
                # print(item, exi)
            i += 1
    
    if impo:
        print("Impossible")