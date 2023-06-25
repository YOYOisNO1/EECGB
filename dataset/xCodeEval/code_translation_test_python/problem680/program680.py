def program680():
    s=input()
    mcount=0
    count=1
    for i in range(len(s)-1):
    	if s[i]==s[i+1]:
    		count+=1
    	else:
    		if count%2==0:
    			mcount+=1
    		count=1
    if count%2==0:
    	mcount+=1
    print(mcount)