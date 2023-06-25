    import sys 
    sys.setrecursionlimit(1000000) 
    n, a, b, c = map( int, input().split())
    
    n = int(n)
    a = int(a)
    b = int(b)
    c = int(c)
    dp = [0 for i in range(n+1)]
    
def ways(n):
        if(n<0 or dp[n]==-1):
            return 0
        
        elif(dp[n] != 0):
           #print( "N: ", n," Memoization: ", dp[n])
           return dp[n]+1
        
        elif(n == 0):
            return 1
    
    
        elif(n>0):
            decisionForputtingMinusValue = max(ways(n-a), ways(n-b), ways(n-c))
            if(decisionForputtingMinusValue == 0):
                dp[n] = -1
            else:
                dp[n] = decisionForputtingMinusValue
            return dp[n]
    
    
    for x in range(1, n+1):
        ways(x)
    
    #print(dp)
    if(dp[n]== -1):
        print(0)
    else:
        print(dp[n])
    #print("length: ", len(dp)) 