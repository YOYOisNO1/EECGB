def program1668():
    x = input()
    y = input()
    if '0' in x:
        m = list(x)
        count = 0
        while '0' in m:
            m.remove('0')
            count+=1
        m.sort()
        x = ''
        for i in m:
            x+=i
        x = x[:1]+'0'*count+x[1:]
    else:
        m = list(x)
        m.sort()
        x = ''
        for i in m:
            x+=i
    if x==y:
        print("OK")
    else:
        print("WRONG_ANSWER")