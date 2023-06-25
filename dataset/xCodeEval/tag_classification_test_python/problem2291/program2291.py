def program2291():
    import sys
    
    if __name__ == "__main__":
    
    	n = int(input())
    
    	if n == 0:
    		sys.stdout.write("O-|-OOOO")
    
    	while n > 0:
    		m = n % 10
    		n /= 10
    		if m >= 5: 	
    			sys.stdout.write("-O|")
    			m -= 5
    		else:
    			sys.stdout.write("O-|")
    		for i in range(m):
    			sys.stdout.write("O")
    		sys.stdout.write("-")
    		for i in range(m, 4):
    			sys.stdout.write('O')
    		sys.stdout.write("\n")
    		