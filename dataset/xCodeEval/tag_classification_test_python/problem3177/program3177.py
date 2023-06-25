    import sys
    
def checkDigit(d):
        x = str(d)
        for y in x:
            if y == '8':
                return True
        else:
            return False
    
    
def solve():
        n = int(sys.stdin.readline())
        ctr = 0
        if checkDigit(n):
            n += 1
            ctr += 1
        while not checkDigit(n):
            n += 1 
            ctr += 1
        print(ctr)
    
    solve()