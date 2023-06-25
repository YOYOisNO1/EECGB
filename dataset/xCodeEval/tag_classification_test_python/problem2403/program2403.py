def program2403():
    from sys import stdin
    data = stdin.readlines()
    n = int(data[0].strip())
    s = data[1].strip()
    
    insk = False
    massin = []
    massout = []
    word = ''
    
    for ch in s:
        if ch=='(':
            if word:
                massout.append(word)
                word = ''
            insk = True
        elif ch==')':
            if word:
                massin.append(word)
                word = ''
            insk = False
        elif ch=='_':
            if word:
                if insk:
                    massin.append(word)
                    word = ''
                else:
                    massout.append(word)
                    word = ''
        else:
            word += ch
    if not s[-1] in ['(', ')', '_']:
        massout.append(word)
    
    maxlen = 0
    for w in massout:
        if len(w)>maxlen:
            maxlen = len(w)
    print(maxlen,) len(massin)
        
            