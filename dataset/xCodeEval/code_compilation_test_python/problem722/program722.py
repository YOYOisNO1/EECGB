def program722():
    s = input()
    x = len(s)
    
    if x%2 == 0:
    	for i in range(1, x):
        	if(s[i] == "1"):
            	print(x//2+1)
            	exit()
     
    print(x//2)
     