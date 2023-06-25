def program2203():
    
    
        a, p = [int(x) for x in input().split()]
         
         
        for i in range(1, 32):
        	# print(i, a-p*i, bin(a-p*i).count('1'))
         
        	if i >= bin(a-p*i).count('1') > 0 and a-p*i >= i:
        		print(i)
        		exit()
         
         
        print(-1)