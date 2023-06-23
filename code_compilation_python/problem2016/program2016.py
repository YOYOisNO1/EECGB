def program2016():
    import math
    num = input()
    numLen = len(num)
    binNums = 0
    restNumsOnes = False
    
    for i, n in enumerate(num):
    	if restNumsOnes == False:
    	    if n == '0':
    	    	continue
    	    elif n == '1':
    	    	binNums += 2**(numLen-i-1)
    	    else n > '1':
    	    	restNumsOnes = True
    	elif restNumsOnes == True:
    		binNums += 2**(numLen-i-1)
    
    print binNums