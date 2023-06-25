    dic={}
def dfs(a,res):
    	if a<=1 and res<=a:
    		return 1
    	elif a*100+res in dic:
    		return dic[a*100+res]
    	else:
    		cnt=0
    		for i in range(a):
    			if i<res-1 and a-i-1<res-1:
    				continue
    			else:
    				cnt=cnt+dfs(i,0)*dfs(a-i-1,res-1)+dfs(i,res-1)*dfs(a-i-1,0)-dfs(i,res-1)*dfs(a-i-1,res-1)
    		dic[a*100+res]=cnt
    		return cnt
    inp=input().split()
    print(dfs(int(inp[0]),int(inp[1])))