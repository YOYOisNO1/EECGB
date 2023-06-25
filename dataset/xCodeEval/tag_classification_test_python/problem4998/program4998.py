def program4998():
    t = int( input() )
    dice_list = [7, 6, 5, 4, 3, 2]
    num_list = []
    
    for i in range(t):
    	x = int(input())
    	num = 0
    	if x <= dice_list[0]:
    		num_list.append(1)
    	else:
    		for dice in dice_list:
    			if x >= dice:
    				num += int(x/dice)
    				x %= dice
    				if x == 0:
    					num_list.append(num)
    					break
    				elif x == 1:
    					num_list.append(num+1)
    					break
    
    for num in num_list:
    	print(num)