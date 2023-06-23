def program3603():
    s = input()
    
    sum = 1
    mulA=10
    
    usedChars = {
    'A' : False,
    'B' : False,
    'C' : False,
    'D' : False,
    'E' : False,
    'F' : False,
    'G' : False,
    'H' : False,
    'I' : False,
    'J' : False,
    }
    
    if s[0] >= 'A' and s[0] <= 'Z':
        usedChars[ s[0] ] = True
        mulA -= 1
        sum *= 9
        
    if s[0] == '?':
        sum *= 9
    
    for ch in s[1:]:
        if ch == '?':
            sum *= 10
        elif not usedChars[ ch ]:
            sum *= mulA
            mulA -= 1
            usedChars[ch] = True
    
    print sum