    # true test: 000100000100000110000000001100
    # 30 sides
    
    
    from fractions import gcd
    
    sides = input()
    factors = [1]
    vals = [int(x) for x in input()]
    hcf = vals[0]
    
    for i in range(2,int(sides**0.5+1)):
        if sides%i == 0:
            factors.append(i)
            if i*i != sides:
                factors.append(sides/i)
    factors = sorted(factors)
    
def setHCF():
        global hcf
        for val in vals:
            hcf = gcd(hcf,val)
            if hcf == 1:
                return
    
    
def simplify():
        for step in factors:
            for start in range(step):
                canGo = True
                sub = 10
                for val in vals[start::step]:
                    if val>0:
                        sub = min(sub,val)
                    else:
                        canGo = False
                        break
                if canGo:
                    for i in range(start,len(vals),step):
                        vals[i] -= sub
    
    
def findImprovement():
        changed = False
        
        toTry = set(i for i in range(side) if vals[i] > 0)
        for step in factors[1:]:
            thisTry = set(a%step for a in toTry)
            for x in thisTry:
        
    ##    for x in range(sides):
    ##        if vals[x] > 0:
    ##            for step in factors[1:]:
                    
                    needUp = [(x+step*i) for i in range(sides/step) if vals[(x+step*i)] == 0]
            #        needUp = []
                    seperation = 0
    ##                for i in range(1,sides/step):
    ##                    if vals[(x+step*i)%sides] == 0:
    ##                        needUp.append((x+step*i)%sides)
                    for i in range(len(needUp)):
                        seperation = gcd(seperation,needUp[i]-needUp[i-1])
                        if seperation < step:
                            break
                    seperation = min(seperation,sides-seperation)
                    if seperation == 0:
                        seperation = factors[-2]
                    if seperation in factors and seperation > step:
                        changed = True
                        start = needUp[0]
                        for i in range(sides/seperation):
                            vals[(needUp[0] + i*seperation)%sides] += 1
                        simplify()
        return changed
                    
                    
    
    setHCF()
    simplify()
    while findImprovement() and sum(vals) != 0:
        pass
    if sum(vals) == 0:
        print 'YES'
    else:
        print 'NO'