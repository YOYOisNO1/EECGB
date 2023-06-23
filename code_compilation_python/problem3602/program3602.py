def program3602():
    s = input()
    
    k = 1
    buk = []
    bu = ['A','B','C','D','E','F','G','H','I','J']
    
    if s[0] in bu:
        k = k*9
        buk = s[0]
    elif s[0] == '?':
        k = k*9
    
    
    for i in range(len(s)):
        if s[i] in bu and buk == []:
            k = k*10
            buk.append(b[i])
        elif s[i] in bu and buk != [] and s[i] not in buk:
            k = k*(10-len(buk))
        elif s[i] == '?':
            k = k*10
    print k