def program3784():
    s = input()
    l = [i for i in s]
    l.append('.')
    l.append('.')
    l.append('.')
    n = len(s)
    p = []
    p.append(s[0])
    i = 1
    f=0
    while i<n:
        if s[i]=='d' and s[i+1]=='o' and s[i+2]=='t':
            p.append('.')
            i+=2
        elif s[i]=='a' and s[i+1]=='t' and f==0:
            p.append('@')
            f=1
            i+=1
        else:
            p.append(s[i])
        i+=1
    #print(p)
    if p[-1]=='.':
        p.pop()
        p.append('d')
        p.append('o')
        p.append('t')
    print(''.join(p))
    