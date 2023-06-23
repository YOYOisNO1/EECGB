    import sys
    
    d0 = [0,0,0,0,1,-1,0,1,-1,0,0]
    
def clucky(x):
        cnt = 0
        while x!=0:
            if x%10 in [4,7]: cnt+=1
            x/=10
        return cnt
        
def solve1(a,add):
        des = clucky(a)+add
        assert des>=0
        b = a+1
        step = 1
        nfree = 0
        while 1:
            while b%(step*10)==0: 
                step*=10
                nfree+=1
            
            tmp = clucky(b/step)
            if tmp+nfree>=des and tmp<=des:
                res = int(str(b/step)+"".join(['0']*(nfree-(des-tmp)))+''.join(['4']*(des-tmp)))
                return res
            b+=step
        assert False
            
def solve(a,l):
        #print "calling",a,l
        if l==1:
            return solve1(a,0)
    
        #with large l, b and a has the same last digit
        res = solve(a/10,(a+l-1)/10-a/10+1)*10+a%10
        if l>=30: return res
    
        #otherwise, there might be more than 1 match:
        for b in range(10):
            if b==a%10: continue
            cur = clucky(a)
            match = True
            pos10 = []
            for i in range(1,min(l,20)):
                next = clucky(a+i)
                if (b+i)%10==0: pos10.append(next-cur)
                elif next-cur!=d0[(b+i)%10]:
                    match = False
                    break
                cur = next
            if match:
                #print a,l,b,pos10
                assert len(pos10)<=1
                if len(pos10)==0:
                    if b>a%10:
                        res = min(res,a-a%10+b)
                    else:
                        res = min(res,solve1(a/10,0)*10+b)
                else:
                    delta = pos10[0]
                    for b2 in range(9): #omiting b2=9
                        if d0[b2+1]!=delta: continue
                        bb = b2*10+b
                        if bb>a%100 and clucky(bb)==clucky(a%100):
                            res = min(res,a-a%100+bb)
                        else:
                            #print a,bb
                            tmp = solve1(a/100,clucky(a%100)+clucky(bb))*100+bb
                            #print tmp
                            res = min(res,tmp)
                            
        #print "Result: ",a,l,res            
        return res
        
    
    fi = sys.stdin
    a,l = map(int,fi.readline().split())
    print solve(a,l)