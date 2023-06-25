def run():
    	import sys
    	sys.stdin = open('/home/punit/Documents/Cpp Programs/input.txt', 'r')
    	sys.stdout = open('/home/punit/Documents/Cpp Programs/output.txt', 'w') 
    	from math import ceil,sqrt,floor
     
    # run()
    
    
    a,b = map(int,input().split())
    
    while a>0 and b>0:
    	if(a>=(2*b)):
    		a = a%(b+b)
    	elif(b>=(2*a)):
    		b = b%(a+a)
    	else:
    		break
    
    print(a,b)