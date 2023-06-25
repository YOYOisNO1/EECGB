    import math
    
    palin = list(input())
    
def ispal(t):
        r = math.floor(len(t)/2)
        for i in range(r):
            if t[i] != t[-i-1]:
                return False
        return True
    
def viab(t):
        count = 0
        r = math.floor(len(t)/2)
        for i in range(r):
            if t[i] != t[-i-1]:
                count +=1
        return count
    
    
    if ispal(palin) == True and len(palin) % 2 == 0:
        print("NO")
    elif ispal(palin) == True:
        print("YES")
    elif viab(palin) == 1:
        print("YES")
    else:
        print("NO")