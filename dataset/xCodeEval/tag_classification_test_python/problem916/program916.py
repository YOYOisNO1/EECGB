def program916():
    #!/usr/bin/python
    
    n = int(input())
    arr = map(int, input().strip().split(" "))
    
    reqSum = sum(arr)/(n/2)
    visited = [False]*n
    
    for i in range(n):
    	if visited[i]==False:
    		visited[i]=True
    		first = i+1
    		temp = i+1
    		req = reqSum-arr[i]
    		while temp<n:
    			if visited[temp]==False:
    				if arr[temp]==req:
    					visited[temp]=True
    					second = temp+1
    					break
    			temp += 1
    		print(first,) second