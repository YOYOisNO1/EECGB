def program6629():
    n = int(input())
    l = [min((-n+90*i)%360,360-(-n+90*i)%360) for i in xrange(4)]
    print(l.index(min(l)))