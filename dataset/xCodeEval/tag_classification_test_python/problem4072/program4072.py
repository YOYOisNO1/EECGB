def program4072():
    
    s=input()
    a = "WUB"
    s2 = " "
    i = 0
    f=False
    while i < len(s):
        x = s[i:i + 3]
        if x == a:
            i += 3
            if f :
              s2 += ' '
              f=False
    
        else:
            s2 += s[i]
            i += 1
            f=True
    
    print(s2[1:])