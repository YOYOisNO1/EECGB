    import sys
def i(): return sys.stdin.readline().strip()
    sys.setrecursionlimit(99999999)
    ii=lambda:map(long,i().split(" "))
    
    a,b=ii()
    bitsA,bitsB=[],[]
    allowed,ac_=[0],0
    z=1
    while z<=a*2:
        if z&a:
            bitsA.append(1)
        else:
            bitsA.append(0)
        if z&b:
            bitsB.append(1)
        else:
            bitsB.append(0)
        z*=2
    #print(bitsB)
    #print(allowed)
def g(adding,ind,acc):
        #print(adding,ind,acc)
        if (acc%adding)^(a%adding)<>0:
            return 0
        rr=0
        if ind==len(bitsB):
            if acc==a:
                rr= 1
            else:
                rr= 0
        elif bitsB[ind]==1:
            a_=g(adding*2,ind+1,acc+adding)
            rr= 2*a_
        else:
            rr= g(adding*2,ind+1,acc)+g(adding*2,ind+1,acc+adding*2)
        return rr
    
    ans= g(1,0,0)
    if a==b:ans-=2
    if b>a:print(0)
    else:print(ans)