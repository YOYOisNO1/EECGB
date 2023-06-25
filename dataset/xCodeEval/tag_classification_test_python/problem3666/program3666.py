def isPrime(n) : 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
      
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                return False
            i = i + 6
      
        return True
    t=int(input())
    while(t>0):
    	a,b=map(int,input().split(" "))
    	
    	if a-b==1:
    		res=a+b
    		# print(res)
    		val=isPrime(res)
    		# print(val)
    		if val==True:
    			print("YES")
    		else:
    			print("NO")
    	else:
    		print("NO")
    	t-=1