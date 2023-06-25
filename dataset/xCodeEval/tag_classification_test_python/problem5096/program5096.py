def program5096():
                                                   # BISMILLAH
                                            # REMEMBER WHY YOU STARTED
    s, sx = input(), input()
    s1, s2 = "", ""
    flag = False
    for i in range(0, len(s)):
        if s[i] == '|':
            flag = True
            continue
        if flag:
            s2 += s[i]
        else:
            s1 += s[i]
    for i in range(0, len(sx)):
        if len(s1) > len(s2):
            s2 += sx[i]
        elif len(s1) < len(s2):
            s1 += sx[i]
        else:
            s1 += sx[i]
    if len(s1) == len(s2):
        print(s1+"|"+s2)
    else:
        print("Impossible")
    
                                # ITS NOT OVER WHEN YOU FAIL, ITS OVER WHEN YOU QUIT
                                                # ITS NOT THE END