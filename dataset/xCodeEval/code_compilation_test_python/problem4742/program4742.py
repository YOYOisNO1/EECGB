    MAX = 101 
    NINF = -22222222222
    base = [-1]*MAX
    dp = [ [ base[:] for i in range(MAX)] for j in range(MAX)] 
    s1 = ""
    s2 = ""
    s3 = ""
    l1 = ""
    l2 = ""
    l3 = ""
    
    
    
def foo(i, j, k):
    	if k == l3 :
    		return "", NINF
    	if i == l1:
    		return "", 0
    	if j == l2:
    		return "", 0
    	if dp[i][j][k] != -1:
    		return dp[i][j][k]
    	ans1, len1 = foo( i + 1, j, k )
    	ans2, len2 = foo( i , j + 1, k )
    	len3 = NINF
    	if s1[i] == s2[j]:
    		if s1[i] == s3[k]:
    			ans3, len3 = foo(i+1, j + 1, k + 1)
    			ans3 += s1[i]
    			len3 += 1
    		else:
    			ans3, len3 = foo(i+1, j + 1, 0 )
    			ans3 += s1[i]
    			len3 += 1
    	if len1 > len2:
    		if len1 > len3:
    			dp[i][j][k] = ans1, len1 
    		else:
    			dp[i][j][k] = ans3, len3
    	else:
    		if len2 > len3:
    			dp[i][j][k] = ans2, len2
    			
    		else:
    			dp[i][j][k] = ans3, len3
    	return dp[i][j][k]
    
    s1 = input()
    s2 = input()
    s3 = input()
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)
    
    ans = foo(0,0,0)
    if ans[1] == 0:
    	print(0)
    else:
    	print(ans[0][::-1]	)