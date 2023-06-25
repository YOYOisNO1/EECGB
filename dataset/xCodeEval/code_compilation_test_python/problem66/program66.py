def program66():
    while 1:
        daysNum=int(input())
        minHolidays=(daysNum//7)*2
        maxHolidays=(daysNum//7)*2
        if daysNum%7 ==1:
            maxHolidays+=1
        elif daysNum%7 >=2:
            maxHolidays+=2
        if daysNum%7 ==6:
            minHolidays+=1
        print(minHolidays,maxHolidays)