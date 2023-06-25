    =list(map(int,input().split()))
    k=0
def prime(p):
    	k=0
    	for i in range(2,p):
    		if p%i==0:
    			k+=1
    			break
    	if k==0:
    		return(True)
    	else:
    		return(False)
    
    if prime(n[0])==False or prime(n[1])==False:
    	print('NO')
    else:
    	for j in range(n[0]+1,n[1]):
    		if prime(j)==True:
    			print('NO')
    			k+=1
    			break
    	if k==0:
    		print('YES')
    
                