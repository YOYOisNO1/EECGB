def gcd(a, b):
    	while(a != 0):
    		temp = a
    		a = b % a
    		b = temp
    	
    	return b
    
def main():
    	string = input()
    	string = string.split()
    	winner = 1
    	
    	a = int(string[0])
    	b = int(string[1])
    	n = int(string[2])
    	
    	parts = [b, a]
    	
    	while(n >= gcd(parts[winner], n)):
    		#print(gcd(parts[winner],) n)
    		n -= gcd(parts[winner], n)
    		
    		if(winner == 0):
    			winner = 1
    		
    		elif(winner == 1):
    			winner = 0
    	
    	print(winner)
    	
    main()