def program2633():
    rotations = int(input().strip())
    valuesPos = []
    valuesNeg = []
    for r in xrange(rotations):
        v = int(input().strip())
        valuesPos.append(v)
        valuesNeg.append(360-v)
    
    valueSums = [valuesPos[0], valuesNeg[0]]
    for i in xrange(1, rotations):
        newSums = []
        for v in valueSums:
            newSums.append(v + valuesPos[i])
            newSums.append(v + valuesNeg[i])
        valueSums = newSums
        
    found = False
    i = 0
    while not found and i < len(valueSums):
        if valueSums[i]%360 == 0:
            found = True
        i++
    if found:
        print("YES")
    else:
        print("NO")