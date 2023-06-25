def program248():
    s = input()
    
    m, b = 0, 0
    for i in s:
        if i.islower():
            m += 1
        else:
            b += 1
    
    if b > m:
        print(s.upper())
    else:
        print(s.lower())