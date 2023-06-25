def program4467():
    l = map(int, str(input()).split())
    for i in l.pop():
        l[0],l[1] = l[1],l[1]+l[0]
    print l[0]