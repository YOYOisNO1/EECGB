def program2563():
    firstEntry = True
    codeNotDone = True
    sameList = False
    numofNums = int(input())
    numbersGiven = []
    numbersGiven = input().split(' ')
    for i in range(0,len(numbersGiven)):
        numbersGiven[i] = int(numbersGiven[i])
        if numbersGiven[i] == 1 and codeNotDone:
            codeNotDone = False
            print(numofNums)
    
    while codeNotDone and not sameList:
        if not firstEntry:
            numbersGiven = n
        else:
            firstEntry = False
        n = sorted(numbersGiven)
        if n[0] == n[-1]:
            sameList = True
        while n[-1] > n[0]:
            n[-1] = n[-1] - n[0]
    if codeNotDone:
        print(n[0]*numofNums)