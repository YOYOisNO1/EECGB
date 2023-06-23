    sx=set()
    for i in range(100004):
    	s.add(i*i)
    global ans
    ans=10000000
    
def f(ii,a):
    	if ii==len(s):
    		x=""
    		for i in range(len(s)):
    			if a[i]==1:
    				x+=s[i]
    		if len(s)>0:
    			if s[0]!='0':
    				if int(x) in sx:
    					ans=min(ans,a.count(0))
    	else:
    		f(ii+1,a+[1])
    		f(ii+1,a+[0])
    
    
    s=input()
    a=[]
    i=0
    f(i,a)
    if ans==10000000:
    	print -1
    else:
    	print ans