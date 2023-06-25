def program1928():
    n=input()
    a=input()
    l=[]
    if n<26:
        print('NO')
    else:
        for i in a:
            if (i.islower() or i.isupper()) and i.lower() not in l:
                l.append(i.lower())
        if len(l)==26:
            print('YES')
        else:
            print('NO')