def main():
    
    	n = int(input())
    	cat =['D','A','C','B']
    	init_cat = cat[n%4]
    	final_cat =init_cat
    	count =0
    	
    	if cat[n%4] <=final_cat:
    		final_cat = cat[n%4]
    		count =0
    	if cat[(n+1)%4]<=final_cat:
    		final_cat = cat[(n+1)%4]
    		count =1
    	if cat[(n+2)%4] <=final_cat:
    		final_cat = cat[(n+2)%4]
    		count =2
    	print(count,final_cat)
    	
    
    
    if __name__ == '__main__':
    	main()