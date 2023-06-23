    a,b,m,r=map(int, input().split())
    if a==1: print m/b
    else:
        Posl=()
    def rand(r):
            return (a*r+b)%m
        r=rand(r)
        while not Posl.count(r):
            Posl+=(r,)
            r=rand(r)
        print len(Posl[Posl.index(r):])
        