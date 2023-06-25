def program420():
    f __name__=="__main__":
    	n,k = map(int,input().split())
    	prime = [2]
    
    	
    	for i in range(3,n):
    		#check if i is prime
    		i_is_prime = True
    		for j in range(2,int(i**0.5)+1):
    			if i%j==0:
    				i_is_prime = False
    				break
    		if i_is_prime:
    			prime.append(i)
    		#check if i can be express as sum of two prime
    	#print(prime)
    	count = 0
    	for i in range(5,n):
    		for j in range(len(prime)):
    			if prime[j]<int(i/2):
    				#print(prime[j]," + ",prime[j+1])
    				if prime[j]+prime[j+1]+1 == i:
    					#print(prime[j],"+",prime[j+1],"+1 =",i,"!!!")
    					count+=1
    					break
    			else:
    				break
    	if(count>=k):
    		print("YES")
    	else:
    		print("NO")