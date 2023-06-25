    import sys, math
def rs():
        return sys.stdin.readline().strip()
def ri():
        return int(sys.stdin.readline().strip())
def ras():
        return sys.stdin.readline().strip().split()
def rai():
        return map(int,sys.stdin.readline().strip().split())
def main():
        x = ri()
        xx = list(str(x))
    def checkn(y):
            yy = list(str(y))
            for j in yy:
                if j in xx:
                    return True
            return False
    
        count = 0
        if x==1:
            return 1
        for i in xrange(1, int(math.sqrt(x))+1):
    
            if not(x%i):
                if checkn(i):
                    count+=1
    
                if checkn(x/i) and i!=x/i:
                    count+=1
    
        return count
    
    
    
    if __name__ == "__main__":
        print(main())