def program4956():
    d={}
    
    for _ in range(3):
    
        s = input()
    
        if '>' in s:
            s = s.replace('>','<')
            s = s[::-1]
    
        a,b = list(s[0::2])
        
        if a in d:
            d[a]+=[b]
        else:
            d[a]=[b]
    
    if len(d)==3:
        print('Impossible')
    else:
        for x in d:
            e = d[x]
            for i in e:
                if i in d:
                    print(x+i+d[i][0])
                    break
            else:
                continue
    
            break