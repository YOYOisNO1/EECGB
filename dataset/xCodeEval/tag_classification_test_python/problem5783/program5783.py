def program5783():
    n=int(input())
    S=input()
    
    DP=[[0]*n for i in range(n)]
    
    for i in range(1,n):
        for j in range(i,n):
            DP[j-i][j]=1+DP[j-i+1][j]
    
            for k in range(j-i+1,j+1):
                if S[k]==S[j-i]:
                    DP[j-i][j]=min(DP[j-i][j],DP[j-i+1][k]+DP[k][j])
    
    print(DP[0][-1]+1)
            
        