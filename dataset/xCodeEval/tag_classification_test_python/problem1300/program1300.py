def removeAt(s, ind):
        return s[:ind] + s[ind + 1:]
    
    
    # s=abcd[z]efg
    
    '''
    s = input()
    i = 0
    while (i < len(s) - 1):
        if s[i] == '/' and s[i + 1] == '/':
            s = removeAt(s, i)
            i -= 1
        i += 1
    n = len(s)
    if n != 1 and s[n - 1] == '/':
        s = removeAt(s, n - 1)
    print(s)
    '''
    s = input()
    sLen, met = len(s), False
    for i in range(sLen - 1):
        if s[i] == '/' and s[i + 1] != '/':
            print('/', end='')
        elif s[i] != '/':
            print(s[i], end='')
            met = True
    if not met or s[sLen - 1] != '/':
        print(s[sLen - 1], end='')
    
    '''
    s = input()
    met = False
    for i in range(len(s) - 1):
        if s[i] == '/' and s[i + 1] != '/':
            print('/')
        elif s[i] != '/':
            met = True
        if not met or s[len(s)-1 != '/'] :
             print(s[len(s)-1])
    '''