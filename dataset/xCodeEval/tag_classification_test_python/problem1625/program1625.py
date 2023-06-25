def program1625():
    str=input()
    
    a=[0 for x in xrange(26)]
    
    max=-1
    
    for i in range(len(str)):
    	k=ord(str[i])-ord('a')
    	a[k]+=1
    	if(k>max):
    		max=k
    
    s=chr(ord('a')+max)*a[max]
    
    print(s)
    	