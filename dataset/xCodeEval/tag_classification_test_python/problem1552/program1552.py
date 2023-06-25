def program1552():
    import sys
    import math
      
    m = int(sys.stdin.readline())
    cm = [int(x) for x in (sys.stdin.readline()).split()]
    x, y = [int(x) for x in (sys.stdin.readline()).split()]
    
    vsum = sum(cm)
    lsum = 0
    res = 0
    for i in range(m - 1, -1, -1):
        lsum += cm[i]
        k = vsum - lsum
        if(k >= x and k <= y and lsum >= x and lsum <= y):
            res = i + 1
            
    print(res)
        