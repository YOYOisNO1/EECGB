    import sys
    m=[]
def madd(*a):
        m.append(sum(map(lambda x: 2**x,a)))
    for i in range(19): 
        madd(i)
def padd(l):
        for i in range(2,len(l)+1):
            for j in range(len(l)-i+1):
                madd(*l[j:j+i])
    
    padd(range(3))
    padd(range(3,7))
    padd(range(7,12))
    padd(range(12,16))
    padd(range(16,19))
    padd([7,12,16])
    padd([3,8,13,17])
    padd([0,4,9,14,18])
    padd([1,5,10,15])
    padd([2,6,11])
    padd([0,3,7])
    padd([1,4,8,12])
    padd([2,5,9,13,16])
    padd([6,10,14,17])
    padd([11,15,18])
    a1 = (input()+input()+' '+input()+input()+input()).split()
    a = zip(a1,[0,3,7]+[1,4,8,12]+[2,5,9,13,16]+[6,10,14,17]+[11,15,18])
    px = sum([2**y for x,y in a if x=='O'],0)
    q = [False]*600000
    m.sort()
    for i in xrange(0,px+1):
        if q[i]: continue
        for p in m:
            if i&p: continue
            q[i|p] = True
            
    print("Karlsson") if q[px] else "Lillebror"
    