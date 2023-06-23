def program2031():
    if __name__ == '__main__':
    	    n=input()
    		m=input()
    		l=len(n)
    		n=list(n)
    		n.sort()
    		i=0
    		while i<l and n[i]=='0':
    			i+=1
    		if i<l and i!=0:
    			n[0]=n[i]
    			n[i]='0'
    		n=''.join(n)
    		if n==m:
    			print "OK"
    		else:
    			print "WRONG_ANSWER"