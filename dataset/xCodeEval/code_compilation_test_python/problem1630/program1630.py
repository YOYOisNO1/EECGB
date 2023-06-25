def program1630():
    input()
    s = input()
    
    a, b = 0, 0
    inP = False
    begin = -1
    pos = -1
    for i in s:
        pos += 1
        if i == '(' || i == ')' || i == '_':
            if begin != -1: # End a word
                if inP:
                    a = max(a, pos - begin)
                else:
                    b += 1
            begin = -1
            if i == '(':
                inP = True
            elif i == ')':
                inP = False
        else:
            if begin == -1:
                begin = pos
    if begin != -1:
        a = max(a, len(s) - begin)
    print a, b