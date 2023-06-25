def program462():
    import math
    
    n = int(input())
    arr = [int(x) for x in input().split()]
    
    numPositive = 0 # want to be greater than or equal n / 2
    numNegatives = 0
    for x in arr:
        if x > 0:
            numPositive += 1
        elif x < 0:
            numNegatives += 1
    
    if numPositive >= int(math.ceil(n / 2)):
        print(1)
    elif numNegatives >= int(math.ceil(n / 2)):
        print(-1)
    else:
        print(0)