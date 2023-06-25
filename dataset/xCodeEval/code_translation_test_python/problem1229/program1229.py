def program1229():
    s=input()
    t=s[0]+s[1:].replace('at','@',1)
    s=t[0]+t[1:-1].replace('dot','.')+t[-1]
    print(s)