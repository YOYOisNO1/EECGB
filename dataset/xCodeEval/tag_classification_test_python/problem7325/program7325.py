    import time
    d1,m1,y1 = input().split('.')
    d2,m2,y2 = input().split('.')
    flag = 0
def is_valid_date(str):
    	try:
    		time.strptime(str, "%d-%m-%y")
    		return True
    	except:
    		return False
    
def solve(d1,m1,y1,d2,m2,y2):
    	if int(y1)-int(y2)>18:
    		return 1
    	elif int(y1)-int(y2)==18:
    		if int(m1)>int(m2):
    			return 1
    		elif int(m1)==int(m2):
    			if int(d1)>=int(d2):
    				return 1
    			else:
    				return 0
    		else:
    			return 0
    
    	else:
    		return 0
    flag = solve(d1,m1,y1,d2,m2,y2)
    if is_valid_date(str(m2)+'-'+str(d2)+'-'+str(y2)):
    	flag+=solve(d1,m1,y1,m2,d2,y2)
    if is_valid_date(str(d2)+'-'+str(y2)+'-'+str(m2)):
    	flag+=solve(d1,m1,y1,d2,y2,m2)
    if is_valid_date(str(y2)+'-'+str(d2)+'-'+str(m2)):
    	flag+=solve(d1,m1,y1,y2,d2,m2)
    if is_valid_date(str(y2)+'-'+str(m2)+'-'+str(d2)):
    	flag+=solve(d1,m1,y1,y2,m2,d2)
    if is_valid_date(str(m2)+'-'+str(y2)+'-'+str(d2)):
    	flag+=solve(d1,m1,y1,m2,y2,d2)
    print('YES') if flag>0 else 'NO'
    
    
    