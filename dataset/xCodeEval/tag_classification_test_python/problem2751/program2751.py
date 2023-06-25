def program2751():
    y = int(input())
    originalIsLeap = False
    startingDay = 1
    tOrF = True
    nextYearHasExtraDay = 0
    
    if (y) % 400 == 0:
        nextYearHasExtraDay = 1
        originalIsLeap = True
    
    
    elif (y) % 4 == 0 and (y) % 100 != 0:
        nextYearHasExtraDay = 1
        originalIsLeap = True
    
    while tOrF:
        #print(str(y) + " " + str(startingDay))
        isLeap = False
        y = y + 1
        startingDay = startingDay + 1 + nextYearHasExtraDay
        nextYearHasExtraDay = 0
        if startingDay > 7:
            startingDay = startingDay - 7
    
        if (y) % 400 == 0:
            nextYearHasExtraDay = 1
            isLeap = True
    
        elif (y) % 4 == 0 and (y) % 100 != 0:
            nextYearHasExtraDay = 1
            isLeap = True
    
        if startingDay == 1 and isLeap == originalIsLeap:
            break
    
    print(y)