    answer = 0
def fn(futdir,h,number):
    	global answer
    	t = 2**(h-1)
    	if(h==1):
    		if(futdir=='right' and number == 2):
    			answer+=1
    		elif(futdir=='right'):
    			answer+=2
    		elif(futdir=='left' and number == 1):
    			answer+=1
    		else:
    			answer+=2
    		return
    	if(futdir=='left'):
    		if(number<=t):
    			answer+=1
    			fn('right',h-1,number)
    		else:
    			answer += 2*t
    			number -= t
    			fn('left',h-1,number)
    	else:
    		if(number>t):
    			number-=t
    			answer+=1
    			fn('left',h-1,number)
    		else:
    			answer+= 2*t
    			fn('right',h-1,number)
    h,number = map(int,input().split())
    fn('left',h,number)
    print(answer)