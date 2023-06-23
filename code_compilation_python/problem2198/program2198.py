def program2198():
    import time
    a,b,m,r=map(int, input().split())
    if a==1:
        time.sleep(0.01)
        print m/b
    else:
        Posl=()
        r= (a*r+b)%m 
        while not Posl.count(r):
            Posl+=(r,)
            r=(a*r+b)%m 
        print len(Posl[Posl.index(r):])
        