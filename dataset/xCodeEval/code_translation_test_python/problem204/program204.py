def program204():
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    prefix=[0]*n
    for i in range(n):
    	prefix[i]=prefix[i-1]+arr[i]
    brr=[]
    for i in range(n):
    	
    	if prefix[i]<=m:
    		print(0,end=" ")
    	else:
    		brr.sort()
    		ct=0
    		sm=prefix[i]
    		# print(brr)
    		for k in range(len(brr)-1,-1,-1):
    			sm-=brr[k]
    			ct+=1
    			if sm<=m:
    				print(ct,end=" ")
    				break
    	brr.append(arr[i])
    print()