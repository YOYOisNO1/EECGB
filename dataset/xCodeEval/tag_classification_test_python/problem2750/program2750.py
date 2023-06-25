def program2750():
    y = int(input())
    S = 0
    if y%400==0 or (y%4==0 and y%100!=0):
    	v=1
    else:
    	v=0
    while True:
    	y+=1
    	if y%400==0 or (y%4==0 and y%100!=0):
    		S+=2
    		Vy = 1
    	else:
    		S+=1
    		Vy=0
    	if S%7==0 and v==Vy:
    		print(y)
    		break
    	