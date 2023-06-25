def satisfies(cnt1, cnt2, onlyX, onlyY, none):
        '''
        tells whether you can form presents using the numbers
        '''
        cnt1 = max(cnt1 - onlyY, 0)
        cnt2 = max(cnt2 - onlyX, 0)
        return (cnt1 + cnt2 <= none)
    
    import sys
    cnt1, cnt2, x, y = map(int, sys.stdin.readline().split())
    bothXY = 0
    onlyX = 0
    onlyY = 0
    none = 0
    v = 0
    while(not satisfies(cnt1, cnt2, onlyX, onlyY, none)):
        v += 1
        if(v % (x * y) == 0):
            bothXY += 1
        elif(v % x == 0):
            onlyX += 1
        elif(v % y == 0):
            onlyY += 1
        else:
            none += 1
    print v