    p1,p2,p3,p4,p5=[[3.830127018922193,3.366025403784439],
    [-3.601321235851749,10.057331467373021],
    [0.466045194906253,19.192786043799030],
    [10.411264148588986,18.147501411122495],
    [12.490381056766580,8.366025403784439]]
    zz=[p1,p2,p3,p4,p5]
    otrx=p3[0]-p1[0]
    otry=p3[1]-p1[1]
    n=int(input())
    lelem=[]
def getind(x,y):
        for n,(xx,yy) in enumerate(lelem):
            if abs(x-xx)<0.000001 and abs(y-yy)<0.0000001:
                return n
        return -1
    for i in xrange(n):
        for x,y in zz:
            if getind(x+i*otrx,y+i*otry)==-1:
                lelem.append((x+i*otrx,y+i*otry))
    po=[]
    for i in xrange(n):
        po.append((-100,)+tuple(getind(x+i*otrx,y+i*otry)+1 for x,y in zz))
    por=[po[0][1]]
    for i in xrange(n):
        por.append(po[i][3])
    for i in xrange(n-1,-1,-1):
        por.append(po[i][5])
        por.append(po[i][2])
        por.append(po[i][4])
        por.append(po[i][1])    
    print len(lelem)    
    for x,y in lelem:
        print str(x).ljust(30,'0'),str(y).ljust(30,'0')
    for x in po:
        print " ".join(map(str,x[1:]))
    print " ".join(map(str,por))            
        