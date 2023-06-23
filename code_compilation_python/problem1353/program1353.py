def ii():  return int(input())
def si():  return input()
def mi():  return map(int,input().strip().split(" "))
def msi(): return map(str,input().strip().split(" "))
def li():  return list(mi())
    
    
    
    n = ii()
    l = li()
    
    s = sum(l)
    if(s%2):
        print(0)
    else:
        dp = []
        ss = s
        s = s//2
        for i in range(n+1):
            dp.append([0]*(s+1))
        for i in range(n+1):
            dp[i][0] = 1
    
        for i in range(1,n+1):
            for j in range(1,s+1):
                if(l[i-1]<=j):
                    dp[i][j] = dp[i-1][j-l[i-1]] or dp[i-1][j]
    
                else:
                    dp[i][j] = dp[i-1][j]
        if(dp[n][s]):
        	print(0)
        else:
    	    for i in range(n):
    	        elif(l[i]%2==0 and dp[n][(ss-l[i])//2] == 0):
    	            print(1)
    	            print(i+1)
    	       
    	            break
    	        elif(l[i]%2):
    	        	print(1)
    	        	print(i+1)
    	        
    	        	break
            