    '''input
    5
    25
    '''
    
    
    
    
def main():
    
    	k = int(input())
    	l = int(input())
    
    	imp = -1
    
    	while(l%k == 0):
    		l = l/k
    		imp += 1
    
    
    	if imp == -1 or l > 1:
    		print("NO")
    	else:
    		print(f"YES\n{imp}")
    
    
    if __name__ == "__main__":
    	main()
    
    
    
    
    
    
    