    
    
def neg (a):
    
        return (-a[0],-a[1])
    
def vplus(a,b):
    
        return (a[0]+b[0],a[1]+b[1])
    
def vecmult(n,v):
    
        return (n*v[0],n*v[1])
    
    
def decide(origin,target,step):
    
    
        movement = vplus(target,neg(origin))
    
        if step[0]==0:
    
            return ((movement[1] % step[1]) == 0) and (movement[0] ==0 ) and (movement[1] * step[1] >0 )
    
        if step[1]==0:
    
            return ((movement[0] % step[0]) == 0) and (movement[1] ==0 ) and (movement[0] * step[0] >0)
    
    
        testvec = vecmult(abs(movement[0]//step[0]),step)
    
        return testvec == movement
    
    
            
    
        
    
    
def main(data=None):
    
    
    
        if data is None:
    
            tgt  = tuple([int(s) for s in (input()).split()])
    
            prog = input()
    
    
            mvs = {'U':(0,1),
                   'D':(0,-1),
                   'L':(-1,0),
                   'R':(1,0)}
    
            if tgt == (0,0):
                return "Yes"
    
    
            vmap =[(0,0),]
    
            for cmnd in prog:
    
                last = vmap[-1]
                cmndv = mvs[cmnd]
    
                vmap.append(vplus(last,cmndv))
    
    
                if vmap[-1] == tgt:
                    return "Yes"
    
    
            step = vmap[-1]
    
            if step ==(0,0):
                return "No"
    
            for v in vmap:
    
                if decide(v,tgt,step):
    
                    return "Yes"
    
    
            return "No"
    
    
    if __name__ =="__main__":
    
        print(main())
            
    
            
        
    
        
            