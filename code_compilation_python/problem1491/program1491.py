def program1491():
    #!/usr/bin/python
    get(N, M, *sk):
    	# N = int(input())
    	#M = int(input())
    	#sk = [0]*101
    	for _ in range(M):
    		a = int(input())
    		sk[a] += 1
    
    	for i in range(M//(N+1), 0, -1):
    		count = 0
    		for j in range(101):
    			count += sk[j]//i
    		if count >= N:
    			print (i)
    			exit()
    
    	print (0)
    	return;
    
    if __name__ = "__main__":
    	data = input()
    	get(*data.split(" "))