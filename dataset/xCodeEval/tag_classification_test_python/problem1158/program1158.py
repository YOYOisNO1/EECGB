def program1158():
    
    numDays, totalTime = input().split()
    
    numDays = int(numDays)
    totalTime = int(totalTime)
    minTotal = 0
    maxTotal = 0
    minTimes = []
    maxTimes = []
    results = []
    
    for x in range(0, numDays):
    	minTime, maxTime = input().split()
    	minTime = int(minTime)
    	maxTime = int(maxTime)
    	minTotal += minTime
    	maxTotal += maxTime
    	minTimes.append(minTime)
    	maxTimes.append(maxTime)
    
    if minTotal <= totalTime and totalTime <= maxTotal:
    	print("YES")
    
    	for y in range(0, numDays):
    		time = min(minTimes[y] + totalTime - minTotal, maxTimes[y])
    		results.append(time)
    		totalTime -= time - minTimes[y]
    
    	for times in results:
    		print(times)
    else:
    	print("NO")
    