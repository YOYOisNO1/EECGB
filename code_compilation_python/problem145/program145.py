def program145():
    if __name__ == '__main__':
    	a,b = map(int, input().split())
    	if a==b:
    		print "infinity"
    		exit()
    	count = 0
    	num = a-b
    	dec = b+1
    	i = 1
    	#print num, dec
    	while dec > b:
    		if num%i==0:
    			#print num,i
    			dec = num/i
    			if dec > b:
    				count+=1
    		i+=1
    	print count