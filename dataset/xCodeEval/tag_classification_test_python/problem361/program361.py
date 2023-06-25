    # helper methods for input
def ri():
        return input()
    
    
def ii(type):
        x = ri()
        if type == 'i':
            return int(x)
        if type == 'l':
            return long(x)
        if type == 'f':
            return float(x)
        if type == 's':
            return str(x)
        return
    
    
def i2(type):
        x = ri().split()
        if type == 'i':
            return int(x[0]), int(x[1])
        if type == 'l':
            return long(x[0]), long(x[1])
        if type == 'f':
            return float(x[0]), float(x[1])
        if type == 's':
            return str(x[0]), str(x[1])
        return
    
    
def ni(type):
        array = ri().split()
    def doforall(x):
            if type == 'i':
                return int(x)
            if type == 'l':
                return long(x)
            if type == 'f':
                return float(x)
            if type == 's':
                return str(x)
            return
        array = map(doforall, array)
        return array
    
    
def pr(array):
    def tostring(el):
            return str(el)
        print(' ').join(map(tostring, array))
    
    
def fndec(x):
        return '{0:.6f}'.format(x)
    
    
    # main
    n = ii('f')
    import math
    print(int(math.ceil(n/2.0)-1))