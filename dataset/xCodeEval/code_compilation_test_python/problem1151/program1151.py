def program1151():
    nums = input().split()
    nums = [int(x) for x in nums]
    
    modded = num[0] % num[1]
    minni = num[0] - modded
    maxx = minni + nums[1]
    
    if nums[0] % num[1] == 0:
        return nums[0]
    
    else:
        total = 0
        start = minni
        while start != 0:
            total += start
            start /= num[1]
        minnii = start
        start = maxx
        total = 0
        while start != 0:
            total += start
            start /= num[1]
        maxxx = total
    if maxxx < minnii:
        return minni
    else:
        return maxx