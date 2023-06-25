    # Get Input
    a = input().split(' ')
    k = int(a[1])
    
    b = input().split(' ')
    p = list(map(int,b))
    
    x = 0
    y = int(a[0]) - 1
    
    # Calculate Number of Problems
def calcX():
        global x
        xflag = 0
        while True:
            if (p[x] > k):
                break
            else:
                if x == y:
                    x = x + 1
                    xflag = 1
                    break
                x = x + 1
        return xflag
    
def calcY():
        global y
        while True:
            if (p[y] > k):
                break
            else:
                if y == x:
                    break
                y = y - 1
    
    while True:
        flag = calcX()
        if (flag):
            break
        calcY()
    
    totalNumber = x + int(a[0]) - y - 1
    
    print(totalNumber)