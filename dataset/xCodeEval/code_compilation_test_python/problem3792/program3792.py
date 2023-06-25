def getDistance(x,y,n):
    	w = (x-1)**2+(y-1)**2
    	b = (x-n)**2+(y-n)**2
    	if w > b:
    		return 'Black'
    	return 'White'
    	
    if __name__=='__main__':
    	n = int(input())
    	t = input().strip().split(' ')
    	x = int(t[0])
    	y = int(t[1])
    	return getDistance(x,y,n)
    	