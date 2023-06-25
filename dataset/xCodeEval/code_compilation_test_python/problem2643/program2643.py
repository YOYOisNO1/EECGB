def program2643():
    import sys
    
    file = sys.stdin
    num = int(file.readline().rstrip())
    sum = 0
    cnt = num - 2
    for i in range(2, num):
    	left = num
    	while left != 0:
    		sum += left%i
    		left /= i
    for i <= min(sum, cnt):
    	if sum%i == 0 and cnt%i == 0:
    		sum /= i
    		cnt /= i
    	else:
    		i += 1
    
    print str(sum) + "/" + str(cnt)
    