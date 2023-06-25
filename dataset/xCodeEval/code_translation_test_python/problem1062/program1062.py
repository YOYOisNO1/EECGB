def program1062():
    suit=input('')
    suit=suit.upper()
    c1,c2,c3,c4,c5=input( ).split(" ")
    if suit[0]==c1[0]or suit[1]==c1[1] or suit[0]==c1[1] or suit[1]== c1[0]:
        print("YES")
    elif suit[0] == c2[0] or suit[1] == c2[1] or suit[0]==c2[1] or suit[1]== c2[0]:
        print("YES")
    elif suit[0] == c3[0] or suit[1] == c3[1] or suit[0]==c3[1] or suit[1]== c3[0]:
        print("YES")
    elif suit[0] == c4[0] or suit[1] == c4[1] or suit[0]==c4[1] or suit[1]== c4[0]:
        print("YES")
    elif suit[0] == c5[0] or suit[1] == c5[1] or suit[0]==c5[1] or suit[1]== c5[0]:
        print("YES")
    else:
        print("NO")