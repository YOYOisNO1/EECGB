def program4266():
    s = input()
    ss = set()
    for i in range(len(s)):
        a = s[-1]+s[0:-1]
        ss.add(a)
        s = a
    
    
    print(len(ss))