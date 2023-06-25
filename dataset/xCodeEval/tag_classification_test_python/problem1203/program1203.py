def win(l,s):
        if l[0]==[s,s,s] or l[1]==[s,s,s] or l[2]==[s,s,s] or l[0][0]==s and l[1][0]==s and l[2][0] == s or l[0][1]==s and l[1][1] == s and l[2][1] == s or l[0][2] == s and l[1][2] == s and l[2][2]==s or l[0][0] == s and l[1][1]==s and l[2][2] == s or l[0][2]==s and l[1][1] == s and l[2][0]==s:
            return 1
        return 0
    
    a = list(input())
    b = list(input())
    c = list(input())
    l = [a,b,c]
    
    mf = a.count("X")+b.count("X")+c.count("X")
    ms = a.count("0")+b.count("0")+c.count("0")
    me = a.count(".")+b.count(".")+c.count(".")
    
    if mf-ms != 0 and mf-ms != 1:
        print("illegal")
    else:
        n = win(l,"0")
        m = win(l,"X")
        if n == 1 and m == 1 or n == 1 and mf-ms != 0 or m == 1 and mf-ms != 1:
            print("illegal")
        elif n == 1:
            print("the second player won")
        elif m == 1:
            print("the first player won")
        else:
            if me == 0:
                print("draw")
            elif mf-ms == 1:
                print("second")
            else:
                print("first")