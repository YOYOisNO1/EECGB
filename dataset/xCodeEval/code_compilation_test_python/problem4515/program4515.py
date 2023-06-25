    m=[2**i for i in xrange(19)]
def madd(*a):
        m.append(sum(map(lambda x: 2**x,a)))
def padd(l):
        for i in range(2,len(l)+1):
            for j in range(len(l)-i+1):
                madd(*l[j:j+i])
    
    a1 = ([0,3,7],[1,4,8,12],[2,5,9,13,16],[6,10,14,17],[11,15,18])
    map(padd,a1+([0,1,2],[3,4,5,6],[7,8,9,10,11],[12,13,14,15],[16,17,18],[7,12,16],[3,8,13,17],[0,4,9,14,18],[1,5,10,15],[2,6,11]))
        
    a = ' '.join(input() for i in xrange(5)).split()
    px = sum([2**y for x,y in zip(a,sum(a1,[])) if x=='O'],0)
    q = [False]*600000
    m.sort()
    for i in xrange(0,px+1):
        if q[i]: continue
        for p in m:
            if i&p: continue
            q[i|p] = True
            
    print "Karlsson" if q[px] else "Lillebror"
    
    