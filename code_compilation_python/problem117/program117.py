def program117():
    #problem link : https://www.codechef.com/LTIME83B/problems/FFL
    import sys 
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    import numpy as np
    #start here
    try:
    	n=int(input())
    	num=list(map(int,input().split()))
    	difflist=np.diff(num)
    	#print(difflist)
    	mlist=[]
    	if len(difflist)<3:
    		print(sum(difflist))
    	else:
    		for i in range(len(difflist)-1):
    			sum1=difflist[i]+difflist[i+1]
    			#print(sum1)
    			#res=difflist[i:i+2]
    			#print(res)
    			#print(max(res))
    			#print((max(sum1,max(difflist))))
    			mlist.append(max(sum1,max(difflist)))
    
    		print(min(mlist))
    except Exception as e:
    	pass
    