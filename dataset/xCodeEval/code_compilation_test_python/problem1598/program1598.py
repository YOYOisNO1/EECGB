def program1598():
    s = input()
    if s[0]!='-':
            print s
    else :
    if s[-1]>s[-2]:
                    s = s[:-1]
            else :  s = s[:-2]+s[-1]
            print int(s)