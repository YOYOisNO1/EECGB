    import math
    ans = dict()
    
def func(a) :
        if a in ans :
            return ans[a]
        ans[a] = (2 ** (a-1))-1
    #    if a==4 :
    #        print "* %d " % ans[a]
        #print "sqrt val %d %d" % (int(math.sqrt(a)), ans[a])
        for i in range(2,int(math.sqrt(a))+1) :
            if a%i==0 :
                ans[a] = ans[a] - func(a/i);                               
                if i != (a/i) : 
                    ans[a] = ans[a] - func(i)
    
    #    print "ans[ %d ] is %d" %(a,ans[a])
        return ans[a]
    
    n,m = input().split()
    n = int(n)
    m = int(m)
    
    if m==n :
        print 1
    elif m%n != 0 :
        print 0
    else :
        a = m/n
        print func(a)