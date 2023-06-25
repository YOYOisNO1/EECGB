def program4798():
    n=int(input())
    t=input()
    gya=[]
    aya=[]
    for k in range(n):
        p=input()
        if p[:3]==t:
            gya.append(p[-3:])
        elif p[-3:]==t:
            aya.append(p[:3])
    
    gya.sort()
    aya.sort()
    if gya==aya:
        print('home')
    else:
        print('contest')
    