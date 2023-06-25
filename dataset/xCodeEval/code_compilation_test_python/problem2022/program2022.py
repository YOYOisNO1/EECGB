def program2022():
    if __name__ == "__main__":
    	n, k = = [int(x) for x in input().split()]
    	Nbr_of_eaten_candies = 0
    	x=1
    	step=1
    	while step < n  :
    		if x+step+1 -(n-step-1) == k :
    			Nbr_of_eaten_candies = n-step-1
    			break
    		x=x+step+1
    		step = step+1 
    	print (Nbr_of_eaten_candies)
    
    