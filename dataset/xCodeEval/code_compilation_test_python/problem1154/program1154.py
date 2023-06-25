def main():
    	n,k=[int(ele) for ele in input().split()]
    	start=1
    	while(True):
    		temp=start
    		count=0
    		while(temp>0):
    			count+=temp
    			temp/=k
    		if(count>=n):
    			break
    		start+=1
    	print start
    
    
    if __name__=="__main__":
    	main()
    