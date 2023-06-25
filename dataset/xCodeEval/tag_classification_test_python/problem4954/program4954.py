def program4954():
    D={'A':0,'B':0,'C':0}
    lt=[]
    for i in range(3):
        str=input()
        if str[1]=='>':
            D[str[0]]+=1
        else:
            D[str[2]]+=1
        lt.append(str)
    win=True
    for i in lt:
        if i[1]=='>':
            if D[i[0]]<=D[i[2]]:
                win=False
        else:
            if D[i[0]]>=D[i[2]]:
                win=False
    if not win:
        print("Impossible")
    else:
        lt=list(D.values())
        lt.sort()
        finalPrint = ""
        for i in lt:
            for j in D.keys():
                if D[j] == i:
                    finalPrint+=j
                    break
        print(finalPrint)