    '''input
    "500 1000 20 30"
    '''
    import sys
def getScore(p,t):
    	p=int(p)
    	t=int(t)
    	return max(3*p, p - (p/250) * t )
    
def findWinner(inputString):
    	varArray=inputString.split()
    	if(getScore(varArray[0],varArray[2]) < getScore(varArray[1],varArray[3])):
    		return "Vasya"
    	elif(getScore(varArray[0],varArray[2]) > getScore(varArray[1],varArray[3])):
    		return "Misha"
    	else: return "Tie"
    
    print(findWinner(input()))