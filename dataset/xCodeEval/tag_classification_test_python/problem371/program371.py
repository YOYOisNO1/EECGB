    m=[];toggleMap={'#':'.','.':'#'}
    YES='YES';NO='NO'
    for i in xrange(4):
    	m.append(list(input().strip()))
    
def isSquare(x,y):
    	if x>2 or y>2:return False
    	return m[x][y]==m[x+1][y]==m[x][y+1]==m[x+1][y+1]
def isInside(x,y):
    	return x>=0 and y>=0 and x<=3 and y<=3
def isSquareArea(x,y):
    	if isInside(x-1,y-1) and isSquare(x-1,y-1):return True
    	if isInside(x-1,y) and isSquare(x-1,y):return True
    	if isInside(x,y-1) and isSquare(x,y-1):return True
    	return isSquare(x,y)
def toggle(x,y):
    	m[x][y]=toggleMap.get(m[x][y],m[x][y])
    
    for x in xrange(4):
    	for y in xrange(4):
    		if isSquare(x,y):
    			print(YES)
    			exit()
    		toggle(x,y)
    		if isSquareArea(x,y):
    			print(YES)
    			exit()
    		toggle(x,y)
    print(NO)