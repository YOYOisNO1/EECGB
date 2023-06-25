def solve():
    	a, b = input().split()
    
    	ans = []
    
    	tmp = ""
    	for i in a:
    		tmp += i
    		cur = ""
    		for j in b:
    			cur += j
    			ans.append(tmp + cur)
    
    	return min(ans)
    
    print(solve())