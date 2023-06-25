def program1596():
    s = input()
    if int(n) < 0 :
        if int(s[:-1]) > int(s[:-2] + s[-1]) : print(s[:-1]))
        else : print(s[:-2] + s[-1])
    else : print(s)