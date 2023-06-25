def find_max(alice,bob):
    	max1=0
    	if(alice[0]>=bob[0]+bob[2]):
    		max1=alice[0]
    	elif(alice[1]>=bob[1]+bob[0]):
    		max1=alice[1]
    	else:
    		max1=alice[2]
    	return max1
    
    
    var=input()
    alice=list(map(int,input().split()))
    bob=list(map(int,input().split()))
    maximum_win=0
    minimum_win=0
    sum1=0
    if(alice[0]>=bob[1]):
    	sum1=bob[1]
    else:
    	sum1=alice[0]
    
    sum2=0
    if(alice[1]>=bob[2]):
    	sum2=bob[2]
    else:
    	sum2=alice[1]
    sum3=0
    if(alice[2]>=bob[0]):
    	sum3=bob[0]
    else:
    	sum3=alice[2]
    
    maximum_win=sum1+sum2+sum3
    index=0
    mainvar=0
    index=alice.index(find_max(alice,bob))
    mainvar=alice[index]
    mainvar-=bob[index]
    if(index==0):
    	mainvar-=bob[2]
    elif(index==1):
    	mainvar-=bob[0]
    else:
    	mainvar-=bob[1]
    
    minimum_win=mainvar
    if(minimum_win<0):
    	minimum_win=0
    print(minimum_win)
    print(maximum_win)
    
    