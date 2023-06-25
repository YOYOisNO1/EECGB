    shoes=input()
    shoes=shoes.split(' ')
    shoes=[int(each) for each in shoes]
    
    
def distinct(array):
    	final=[]
    	for each in array:
    		if each not in final:
    			final.append(each)
    	if(len(final)>3):
    		return 4
    	else:
    		return len(final)
    ans=4-distinct(shoes)
    print(ans)