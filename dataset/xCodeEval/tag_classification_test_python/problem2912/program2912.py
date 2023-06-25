def program2912():
    n=int(input())
    y=input()
    s=''
    cnt=0
    ans=n
    for i in y:
    	cnt+=1
    	s+=i
    	t=s+s
    	res=cnt+1
    	for j in range(len(t),n):
    		t+=y[j]
    		res+=1
    	if y==t:
    		ans=min(ans,res)
    print(ans)