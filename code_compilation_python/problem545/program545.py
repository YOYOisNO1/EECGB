def program545():
    s = map(str,input().split())
    s = list(s)
    x = int(s[0])
    if s[2]=='week':
        if x==5 or x==6:
            print("53")
        else:
            print("52")
    else:
        if x<30:
            print("12")
        elif x==30
            print("11")
        else:
            print("7")
    