def program1649():
    qwerty = 'qwertyuiopasdfghjkl;zxcvbnm,./'
    
    keyToInt = {}
    count = 0
    for c in qwerty:
        keyToInt[c] = count
        count += 1
    
    intToKey = {}
    
    for i in range(len(qwerty)):
        intToKey[i] = qwerty[i]
    
    
    R = lambda: input()
    d = R()
    s = list(R())
    
    for i in range(len(s)):
        if d == 'R':
            s[i] = intToKey[keyToInt[s[i]] - 1]
        else:
            s[i] = intToKey[keyToInt[s[i]] + 1]
    
    print('').join(s)
    
    
    
    
    
    