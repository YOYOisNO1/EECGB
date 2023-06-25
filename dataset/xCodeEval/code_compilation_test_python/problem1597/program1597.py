def program1597():
    s = input()
    if int(s) < 0 :
        if int(s[:-1]) > int(s[:-2] + s[-1]) : print(s[:-1]))
        else : print(s[:-2] + s[-1])
    else : print(s)