    NAME = "P1"
    try:
        inFile = open(NAME+".txt")
    except:
        pass
    
def read():
        try:
            return inFile.readline().strip()
        except:
            return input().strip()
    
    n,m = map(int,read().split())
    if n>m:
        n,m = m,n
    if n == 1:
        print(n*m)
    elif n == 2:
        print((2*(m/4)) + min(2,m%4))*2
    else:
        if (n*m)%2 == 0:
            print(n*m/2)
        else:
            print(n*m/2+1)