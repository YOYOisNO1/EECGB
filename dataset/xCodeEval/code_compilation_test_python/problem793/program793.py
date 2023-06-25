def program793():
    m, d = map(int, input().strip().split(" "))
    
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
    num = days[m]
    num += d-1
    if num % 7 == 0:
    	if m == 2:
    		print 4
    	else:
    		print 5
        exit()
    print (num + 6) / 7