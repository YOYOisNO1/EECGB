def main():
    	ans = [[0 for x in range(200)] for y in range(200)]
    
    	n,m,k,x,y=map(int,input().split())
    
    	if n==1:
    		if k%m==0:
    			print (k//m,k//m,k//m)
    		else:
    			vl=0
    			if y<=(k%m):
    				vl=k//m+1
    			print (k//m+1,k//m,vl)
    		return 
    
    
    	ma=-1*(10**20)
    	mi=(10**20)
    
    	xloc=0
    	yloc=0
    
    	for i in range(1,n+1):
    		
    		for j in range(1,m+1):
    			
    			lo=0		
    			hi=10**18		
    			increment1=2*(n-i)*m		
    			increment2=2*(i-1)*m
    			
    			while hi-lo>1:
    				mid=(int)((lo+hi)/2)
    
    				times2=(int)(mid/2)
    
    				if(increment2==0):
    					times2=0
    
    				times1=mid-times2
    				
    				if(increment1==0):
    					times1=0
    					times2=mid
    
    				sumtotal=(i-1)*m+j+increment1*times1+increment2*times2
    
    				if sumtotal<=k:
    					lo=mid
    
    				else:
    					hi=mid-1
    
    			times2=hi/2
    
    			if increment2==0:
    				times2=0
    
    			times1=hi-times2
    
    			if increment1==0:
    				times1=0
    				times2=hi
    
    			sumtotal=(i-1)*m+j+increment1*times1+increment2*times2
    
    			if sumtotal<=k:
    				ans[i][j]=hi+1
    
    			else:
    				ans[i][j]=lo+1
    			
    			#print (ans[i][j])
    			if(ma<ans[i][j]):
    				xloc=i
    				yloc=j
    			ma=max(ma,ans[i][j])
    			mi=min(mi,ans[i][j])
    
    
    		#print ("")
    	#print (xloc,yloc)
    	print (ma,mi,ans[x][y])
    	return
    
    main()