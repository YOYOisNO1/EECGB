def right(L):
        d1 = (L[4]-L[2])**2+(L[3]-L[1])**2
        d2 = (L[6]-L[2])**2+(L[5]-L[1])**2
        d3 = (L[6]-L[4])**2+(L[5]-L[3])**2
        if d1*d2*d3 == 0:
            return False
        elif (d1+d2 == d3):
            return True
        elif d1+d3 == d2:
            return True
        elif d2+d3 == d1:
            return True
        else:
            return False
    L = [0]+[int(x) for x in input().split()]
def aright(L):
        for i in range(1,7):
            temp = L[:]
            temp[i] += 1
            if right(temp):
                return True
            temp[i] += -2
            if right(temp):
                return True
        return False
    
    if right(L):
        print('RIGHT')
    elif aright(L):
        print('ALMOST')
    else:
        print('NEITHER')