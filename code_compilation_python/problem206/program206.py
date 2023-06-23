    from sys import stdin,stdout
    
def main():
    	string=stdin.readline()
    	sum=0
    
    	for i in range (len(string)-1):
    		if i==0:
    			p=ord(string[0])-97
    			if p>13:
    				sum+=(26-p)
    			else:
    				sum+=p
    		else:
    			p=abs(ord(string[i])-ord(string[i-1]))
    			print(sum)
    			if p>13:
    				sum+=26-p
    			else:
    				sum+=p
    
    	print(sum)
    
    if __name__ == '__main__':
    	main()