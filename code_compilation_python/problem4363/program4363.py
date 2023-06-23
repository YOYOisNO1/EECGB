    import sys
    
    d0 = [0,0,0,0,1,-1,0,1,-1,0,0]
    oo = 1000000000000
def clucky(x):
        cnt = 0
        while x!=0:
            if x%10 in [4,7]: cnt+=1
            x/=10
        return cnt
        
def solve1(a,add):
        des = clucky(a)+add
        if des<0:
            return oo
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
           
def agree(a,b,l):
        for i in range(l-1):
            if clucky(a+i+1)-clucky(a+i)!=clucky(b+i+1)-clucky(b+i):
                return False
        return True
        
def solve(a,l):
        #print "calling",a,l
        if l==1:
            return solve1(a,0)
    
        #with large l, b and a has the same last digit
        res = solve(a/10,(a+l-1)/10-a/10+1)*10+a%10
        if l>=30: return res
    
        #otherwise, there might be more than 1 match:
        for b0 in range(10):
            for b1 in range(9):
                step = 10
                for n9 in range(20):
                    b = b0+step-10+step*b1
                    step2 = 10*step
                    if b>res: break
                    if agree(a,b,l):  
                        if b>a%step2 and clucky(b)==clucky(a%step2):
                            res = min(res,a-a%step2+b)
                        else:
                            tmp = solve1(a/step2,clucky(a%step2)-clucky(b))*step2+b
                            res = min(res,tmp)
                        #print b,res
                    step*=10
                    
                            
        #print "Result: ",a,l,res            
        return res
    
    fi = sys.stdin
    a,l = map(int,fi.readline().split())
    print solve(a,l)
    
    
    '''
    print solve(499999977,395) #500000777
    print solve(3997,3) #4999
    print solve(485449,2) #485454
    print solve(4876,2)#48783
    print solve(77,2) #144
    print solve(777,10) #1447
    print solve(469,1) #480
    print solve(7,4)#17
    print solve(4,7)#14
    print solve(10,10)#20
    print solve(47,74) #147
    '''