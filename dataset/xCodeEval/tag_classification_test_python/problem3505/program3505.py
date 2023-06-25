def f(n):
        if n<10:
            return('0'+str(n))
        return str(n)
    sth,stm = map(int,input().split(":"))
    eth,etm = map(int,input().split(":"))
    ht, mt = eth - sth, etm - stm
    s1 = ht*60 + mt
    s1 //=2
    ansh = sth+(s1//60)
    ansm = stm+(s1%60)
    if ansm>=60:
        ansm=ansm%60
        ansh+=1
    print(f"{f(ansh)}:{f(ansm)}")