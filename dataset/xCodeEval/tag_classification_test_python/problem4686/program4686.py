def program4686():
    import string
    l=lambda:map(int,input().split())
    n,k=l()
    s=input()
    t=[]
    for c in string.uppercase:
        first=s.find(c)
        if first==-1:
            continue
        t.append((first,'f',1))
        last=s.rfind(c)
        t.append((last,'l',-1))
    t.sort()
    personNeeded=0
    for a,b,c in t:
        personNeeded+=c
        if personNeeded>k:
            print('YES')
            exit()
    print('NO')