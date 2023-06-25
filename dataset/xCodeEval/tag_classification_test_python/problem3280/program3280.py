    b = int(input()) +1
    inn = list(map(int,input().split(" ")))
    inn.append(90)
def ff():
    	if(inn[0]>15):
    		return 15
    	for a in range(1,b):
    		if (inn[a] - inn[a-1]) >15:
    			return(inn[a-1] + 15) 
    	return(90)
    print(ff())