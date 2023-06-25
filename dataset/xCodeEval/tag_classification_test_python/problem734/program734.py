def program734():
    a=['','','','','','','','']
    for i in range(8):
        s=input()
        r=0
        for j in s:
            a[r]+=j
            r+=1
    Akmin,Bkmin=100,100
    for i in a:
        Ak,Bk=0,200
        for j in i:
            if j=='B':
                Bk=0
                Ak=200
            if j=='W':
                Bk=200
                if Ak<Akmin:
                    Akmin=Ak
            if j=='.':
                Ak+=1
                Bk+=1     
        if Bk<Bkmin:
            Bkmin=Bk
    if Akmin<=Bkmin:
        print('A')
    else:
        print('B')