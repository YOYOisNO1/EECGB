    import sys
    
def xx(aa, bb):
            
        a, b = aa, bb
        while a!=0 and b!=0:
            if a>b:
                a = a % b
            else:
                b = b % a
        return (a+b)
        
def solve(x, y, n):
        d = xx(x, y)
        x /= d
        y /= d
        
        if n>=y:
            return str(x) + "/" + str(y)
        #perebor?
        #delta =
        drob = float(x) / y
        cur = 1
        if drob % 1 == 0.5
            chi = int(drob)
        else:
            chi = int(round(drob))
        
        delta = drob
        
        for i in xrange(2, n+1):
            new_chi = int(round(float(x) * i / y))
            new_delta = abs(new_chi/float(i) - drob)
            if new_delta < delta and (chi*i!=new_chi*cur):
                delta = new_delta
                cur = i
                chi = new_chi
                #print str(chi) + "/" + str(cur) + "->" + str(delta)
        return str(chi) + "/" + str(cur)
    
    
    x, y, n = map(int, sys.stdin.readline().split())
    #print x, y, n
    print solve(x, y, n)
    