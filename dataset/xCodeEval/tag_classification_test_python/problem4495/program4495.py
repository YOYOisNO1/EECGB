def program4495():
    import sys
    
    
    if __name__ == '__main__':
    	s=input()
    	
    	s=list(s)
    	if(len(s)<26):
    		print(-1)
    	else:
    		ch='a'
    		flg=False
    		lst=map(chr,range(97,123))
    		i=0
    		for idx in range(len(s)):
    			if (i<26 and s[idx]<=lst[i]):
    				s[idx]=lst[i]
    				i+=1
    		if i==26:
    			s=''.join(s)
    			print(s)
    		else:
    			print(-1)
    
    
    
    
    
    
    
        
    
        