def program2393():
    s = list(input())
    
    count = 0
    changed = False
    
    for i in range(len(s)):
        if len(s) == 1:
            break
        if i < len(s)-1 and s[i] == 'V' and s[i + 1] == 'K':
            count += 1
            #print(i, 'a')
            continue
        if changed == False:
            if i == 0:
                if s[i] == 'K' and s[i+1] == 'K':
                    s[i] = 'V'
                    count += 1
                    changed = True
                    #print(i, 'b')
            elif i != len(s)-1:
                if s[i] == 'K':
                    if s[i-1] != 'V' and s[i+1] == 'K':
                        s[i] = 'V'
                        count += 1
                        changed = True
                        #print(i, 'c')
                        continue
                else:
                    if s[i-1] == 'V' and s[i+1] != 'K':
                        s[i] = 'K'
                        count += 1
                        changed = True
                        #print(i, 'd')
                        continue
            elif s[i] == 'V' and s[i-1] == 'V':
                s[i] = 'K'
                count += 1
                #print(i, 'e')
    print(count)