def program3745():
    n = int(input())
    ds = list(map(int, input()))
    found = False
    
    for i in range(0, sum(ds)+1):
        l = 0
        curSum = 0
    
        intervals = 0
        
        while l < n:
            curSum += ds[l]
            if curSum > i:
                break
            if curSum == i:
                curSum = 0
                intervals += 1
            l += 1
        
        if curSum == 0 and intervals >= 2:
            found = True
            break
    
    print(['NO', 'YES'][found])