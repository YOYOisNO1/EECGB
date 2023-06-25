def program3294():
    s=input().strip()
    
    con1, con2 = 'http://', 'ftp://'
    
    if s[0]=='h':
    	start= 4
    	end = 4
    	for i in range(4,len(s)-1):
    		if s[i]+s[i+1] == 'ru' && start !=end:
    			end = i
    			break
    	ans = s[start:end]
    
    	ans = con1+ans+'.ru/'+s[end+2:]
    	print(ans)
    
    elif s[0]=='f':
    	start= 3
    	end = 3
    	for i in range(3,len(s)-1):
    		if s[i]+s[i+1] == 'ru' && start !=end:
    			end = i
    			break
    	ans = s[start:end]
    
    	ans = con2+ans+'.ru/'+s[end+2:]
    	print(ans)