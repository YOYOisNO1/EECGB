def program328():
    n, k = map(int, input().split())
    
    ini = 1
    
    while True:
        tempStr = str(n*ini)
        zero = 0
        for i in xrange(len(tempStr)-1, -1, -1):
            if tempStr[i] == '0':
                zero += 1
            else:
                break
        if zero >= k:
            print tempStr
            exit()
        ini += 1