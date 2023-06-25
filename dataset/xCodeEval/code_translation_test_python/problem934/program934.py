def program934():
    num = input()
    
    stringNum = num[0] + num[2] + num[4] + num[3] + num[1]
    
    intNum = int(stringNum)
    intNum = intNum ** 5
    
    stringNum = str(intNum)
    
    print(stringNum[len(stringNum)) - 5] + stringNum[len(stringNum) - 4] + stringNum[len(stringNum) - 3] + stringNum[len(stringNum) - 2] + stringNum[len(stringNum) - 1]