def program246():
    s = input()
     
    upL = 0
    loL = 0
     
     
    for ch in s:
        if ch.islower():
            loL = loL + 1
        if ch.isupper():
            upL = upL + 1
            
    if upL > loL:
        print(s.upper())
    elif loL > upL:
        print(s.lower())
    else:
        print(s.lower())