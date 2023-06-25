def program2327():
    numbers = input ()
    space = numbers.find (" ")
    redsock = int(numbers[0:space])
    bluesock = int (numbers[space:len(numbers)])
    days = 0
    afterdays = 0
    counter = 0
     
    while counter == 0:
        if (redsock >= 1) and (bluesock >= 1):
            days = days + 1
            redsock = (redsock - 1)
            bluesock = (bluesock - 1)
        else:
            if redsock == 0:
                afterdays = (bluesock//2)
            if bluesock == 0:
                afterdays = (redsock//2)
            counter = 1
            
    print((str(days)) + " " + str(afterdays))