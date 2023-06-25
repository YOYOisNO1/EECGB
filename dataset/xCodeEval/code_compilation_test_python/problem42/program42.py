    li = list(map(int,input().split()))
    n = li[0]
    t = li[1]
    l1 = [0]
    l2 = [0,0]
    l3 = [0,0,0]
    l4 = [0,0,0,0]
    l5 = [0,0,0,0,0]
    l6 = [0,0,0,0,0,0]
    l7 = [0,0,0,0,0,0,0]
    l8 = [0,0,0,0,0,0,0,0]
    l9 = [0,0,0,0,0,0,0,0,0]
    l10 = [0,0,0,0,0,0,0,0,0,0]
    Levels = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
    #print("n,t",n,t)
def pour(Levels,level, glass, index):
    	#print("pour(Levels,level,glass,index)")
    	#print("Levels avant : ")
    	#print(Levels)
    	#print(level, glass, index)
    	if(Levels[level][index]==1):
    		if(level!=9):
    			pour(Levels,level+1,glass/2,index)
    			pour(Levels,level+1,glass/2,index+1)
    	else:
    		Levels[level][index]+=glass
    	#print("Levels après :")
    	#print(Levels)
    
def verresremplies(levels,niveaux):
    	count=0
    	for level in range(niveaux):
    		for valueGlass in levels[level]:
    			if (valueGlass==1):
    				count+=1
    	return(count)
    
    for i in range(1,t+1):
    	#print("\n\n\n\n")
    	#print("temps i : ",i)
    	#print("\n\n\n\n")
    	pour(Levels,0,1,0)
    
    print(verresremplies(Levels,n))