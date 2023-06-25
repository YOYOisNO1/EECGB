    n=int(input())
    s=input()
    sl = len(s)
    l=[]
def rec(i):
    	if(i>=sl):
    		tot=0
    		mul = 1
    		for i in range(len(l)-1,-1,-1):
    			tot+=(mul*l[i])
    			mul*=n
    		return tot
    	if(s[i]=='0'):
    		l.append(0)
    		tot = rec(i+1)
    		del l[len(l)-1]
    		return tot
    	j=1
    	ans = 1000000000000000000000000000
    	while(i+j<=sl):
    		num = int(s[i:i+j])
    		if(num>=n):
    			break
    		l.append(num)
    		ans = min(ans,rec(i+j))
    		del l[len(l)-1]
    		j+=1
    	return ans
    print(rec(0))
    