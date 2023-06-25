def par(phrase):
        ic, oc, max_oc = 0,0,0
        maxoc = 0
        inside = False
        found = False
        for i, x in enumerate(phrase):
            if x == '(':
                if found:
                    oc += 1
                found = False
                inside = True
            elif x == ')':
                if found:
                    p = i+1
                    ic += 1
                found = False
                inside = False
            elif x == '_':
                if not found:
                    continue
                if inside:
                    ic += 1
                else:
                    oc += 1
                found = False
            else:
                if not found:
                    p = i
                found = True
                if not inside:
                    maxoc = max(maxoc,i-p+1)
        if found and inside:
            ic += 1
        return maxoc, ic
    
    input()
    phrase = input().rstrip()
    print('%d %d') % par(phrase)