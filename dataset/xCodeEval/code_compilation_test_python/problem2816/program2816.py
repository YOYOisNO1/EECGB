    a, b = map(int, input().split())
    
def checkDigits(x):
        return (len(str(x)) == len(set(str(x))))
    
    for i in range(a,b+1):
        if checkDigits(i):
            return i
        
    return -1