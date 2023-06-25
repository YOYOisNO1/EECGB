    
    numbers = input()
    
    numbers = [n for n in map(lambda n: int(n), numbers)]
    
    
def check_lucky(list):
        #print((list,) sum(list[:3]), sum(list[3:]), sum(list[:3]) == sum(list[3:]))
        return sum(list[:3]) == sum(list[3:])
    
    if check_lucky(numbers):
        print(0)
        exit()
    
    
    
def incDigit(x):
        x += 1
        if x > 9:
            x = 0
        return x
    
    minReplaced = 7
    replaced = 0
    index = 0
def checkForDigit(index, list, replaced):
        global minReplaced
        #print((index))
        replaced += 1
        for x in range(10):
            if x != numbers[index]:
                list[index] = x
                if check_lucky(list):
                    minReplaced = min(replaced, minReplaced)
    
    #check for one
    for i in range(6):
        newNumbers = [x for x in numbers]
        checkForDigit(i, newNumbers, 0)
    if minReplaced == 1:
        print(1)
        exit()
    
    #check for two
    #print('check two')
    for i in range(6):
        newNumbers = [x for x in numbers]
        for t in range(10):
            if t != numbers[i]:
                #print(('i) ', i)
                newNumbers[i] = t
                for z in range(i, 6, 1):
                    #print('checking second index ', z)
                    newNumbers2 = [y for y in newNumbers]
                    checkForDigit(z, newNumbers2, 1)
    
    if minReplaced == 2:
        print(2)
        exit()
    
    print(3)