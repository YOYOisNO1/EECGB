def program4270():
    s = input()
    o = set()
    for i in range(len(s)):
        o.add(s)
        s = s[-1] + s[:-1]
        #print(s)     #it will give the cyclic order
    print(len(o))