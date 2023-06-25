def program1916():
    n = input()
    poke_list = []
    pokecross = input("")
    if n==6:
        print "espeon"
    elif n==7 and pokecross[3] != 'r':
        poke_list.append("sylv")
        poke_list.append("leaf")
        poke_list.append("glac")
        poke_list.append("jolt")
        poke_list.append("umb")
        poke_list.append("fla")
        for pokename in poke_list:
            i = 0;
            for character in pokename:
                if pokecross[i] != character:
                    i=i+1
                elif (i==2 and pokecross[i] == 'a') or (i==1 and pokecross[i] =='l'):
                    i=i+1
                elif pokename[0]=='f' of pokename[0]=='u':
                    print pokename + "reon"
                    break
                else:
                    print pokename + "eon"
                    break
    else:
        print "vaporeon"