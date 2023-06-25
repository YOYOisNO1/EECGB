    n = int(input())
    perfect = []
def dfs(dig,rm):
    	if dig == 0:
    		return [rm]
    
    	if rm == 0:
    		return [0]
    
    	elif dig == 1 and rm == 10:
    		tmp = []
    		for i in range(1,10):
    			for j in dfs(dig-1,rm-i):
    				num = j + i * (10 **(dig))
    				tmp.append(num)
    
    		return tmp
    
    	else:
    		tmp = []
    		for i in range(rm+1):
    			if i == 10:
    				break
    			for j in dfs(dig-1,rm-i):
    				num = j + i * (10 **(dig))
    				tmp.append(num)
    
    		return tmp
    		
    
    for num in dfs(7,10):
    	perfect.append(num)
    
    
    print(perfect[n-1])
    #print(perfect[n-1])
    #print(per)