    
def resolve():
    	bags_in = input("enter 4 bags: ")
    	bags = list(map(int, bags_in.split()))
    	friend1 = []
    	friend2 = 0
    	for candie1 in bags:
    		for candie2 in bags[1:]:
    			friend1.append(candie1)
    			friend1.append(candie2)
    			a = list(set(bags) - set(friend1))
    			friend2 = sum(a)
    			print(friend1)
    			print(friend2)
    			if sum(friend1) == friend2:
    				return True
    			friend2 = 0
    			friend1.clear()
    	return False
    
    if(resolve()){
    	print("YES")
    } else {
    	print("NO")
    }