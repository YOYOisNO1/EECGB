def program4298():
    
    
    s = input()
    k = int(input())
    chars = [i for i in s if i != '*' and i != '?']
    
    candy = 0
    snow = 0
    
    for i in s:
        if i == '?':
            candy += 1
        if i == '*':
            snow += 1
    
    if k == len(chars):
        print(''.join(chars))
    
    elif k < len(chars):
        if candy + snow < len(chars) - k:
            print("Impossible")
        else:
            diff = len(chars) - k
            c = [i for i in s]
            i = 0
            while i < len(c) and diff > 0:
                if candy > 0 and c[i] == '?':
                    c[i] = -1
                    c[i-1] = -1
                    diff -= 1
                    candy -= 1
    
                elif snow > 0 and c[i] == '*' and diff > 0:
                    c[i] = -1
                    c[i-1] = -1
                    diff -= 1
                    snow -= 1
                i += 1
    
            ans = [i for i in c if i != -1 and i != '*' and i != '?']
            print(''.join(ans))
    
    else:
        if snow == 0:
            print('Impossible')
        else:
            diff = k - len(chars)
            c = [i for i in s]
            for i in range(len(c)):
                if c[i] == '*':
                    while diff > 0:
                        c.insert(i,c[i-1])
                        diff -= 1
                    break
    
            ans = [i for i in c if i != '*' and i != '?']
            print(''.join(ans))
    
    
    