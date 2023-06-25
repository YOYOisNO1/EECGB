def program3586():
    n,t=map(int,input().split())
    # s = list(map(int,input().split('+')))
    s=input()
    a=[]
    out=[]
    
    for i in range(n):
    	a.append(s[i])
    	out.append(s[i])
    cnt=t
    while t:
    	i=0
    	while i<n-1:
    
    		if out[i]=='B' and out[i+1]=='G':
    			out[i+1]='B'
    			out[i]='G'
    			i+=2
    		else:
    			i+=1
    	t-=1
    
    ans=''
    for i in range(n):
    	ans+=out[i]
    
    print(ans)
    
    