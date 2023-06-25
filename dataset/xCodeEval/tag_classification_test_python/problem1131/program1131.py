def program1131():
    n = input()
    ls = map(int,input().split())
    read = 0
    
    day = 1
    
    while True:
    	read = read + ls[day-1]
    
    	if read >= n:
    		print(day)
    		break
    	else:
    		day = day + 1
    		if day == 8:
    			day = 1
    			