def program729():
    import math 
    
    #enumerations and constructing subsets , subsets and enumerations 
    
    t = int(input())
    
    if(t<=9):
    	print t
    
    elif(t>9 and t <= 189):
    	if((t-9)%2==0):
    		print (9 + int(math.ceil((t-9)/2)))%10
    	else:
    		print (9 + int(math.ceil((t-9)/2))%10               #somewhere kinda invalid syntax 
    
    
    