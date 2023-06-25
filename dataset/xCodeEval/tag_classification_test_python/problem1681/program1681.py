def check(i, n, x, y, s, dp):
    	# print(i, chr(x+97), chr(y+97))
    	if i==n:
    		return 1
    	if dp[i][x][y]!=-1:
    		return dp[i][x][y]
    	
    	ch = ord(s[i])-97
    	dp[i][x][y] = 0
    
    	if ch>=x and check(i+1, n, ch, y, s, dp)>0:
    		dp[i][x][y] = 1
    	elif ch>=y and check(i+1, n, x, ch, s, dp)>0:
    		dp[i][x][y] = 2
    	
    	return dp[i][x][y]
    
    if __name__ == "__main__":
    	n = int(input())
    	s = input()
    
    	dp = [[[-1]*26 for j in range(26)] for i in range(n)]
    	if check(0, n, 0, 0, s, dp)==0:
    		print("NO")
    	else:
    		print("YES")
    		ans = ''
    		x = 0
    		y = 0
    		for i in range(n):
    			ch = ord(s[i])-97
    			ans += str(dp[i][x][y]-1)
    			if dp[i][x][y]==1:
    				x = ch
    			else:
    				y = ch
    		print(ans)