def program264():
    n=int(input())
    s=str(input())
    x=['a','e','i','o','u','y']
    i=0;
    while(i<len(s)-2):
    	if(s[i] in x and s[i+1] in x):
    		s=s[:i+1]+s[i+2:]
    	else:
    		i+=1
    if(s[i] in x and s[i+1] in x):
    	print(s[:i+1])
    else:
    	print(s)				