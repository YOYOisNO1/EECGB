    uASei = range
    uASeU = print(uASeg) = list
    uASeo = map
    uASey = int
    uASeH = input
    
    
def uASef(p):
        a = (p[0]-p[2])**2+(p[1]-p[3])**2
        b = (p[0]-p[4])**2+(p[1]-p[5])**2
        c = (p[2]-p[4])**2+(p[3]-p[5])**2
        return a and b and c and (a + b == c or a + c == b or b + c == a)
    
    
def uASex(p):
        if uASef(p):
            return 'RIGHT'
        for i in uASei(6):
            p[i] -= 1
            if uASef(p):
                return 'ALMOST'
            p[i] += 2
            if uASef(p):
                return 'ALMOST'
            p[i] -= 1
        return 'NEITHER'
    
    
    uASeU(uASex(uASeg(uASeo(uASey, uASeH().split()))))