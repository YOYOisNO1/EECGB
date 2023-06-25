    from sys import stdin, stdout
    from collections import Counter, defaultdict
    from itertools import permutations, combinations
    input = stdin.readline
    pr = stdout.write
    
    
def in_arr():
        return map(int,input().split())
    
    
def pr_num(n):
        stdout.write(str(n)+'\n')
    
    
def pr_arr(arr):
        pr(' '.join(map(str,arr))+'\n')
    
    
    range = xrange # not for python 3.0+
    
    # main code
    
    w,b=in_arr()
    
    dp=[[0 for i in range(w+1)] for i in range(b+1)]
    vis=[[0 for i in range(w+1)] for j in range(b+1)]
    dp[b][w]=1
    vis[b][w]=1
    q=[(b,w)]
    ans=0
    while q:
        x,y=q.pop(0)
        
        if x:   
            if not vis[x-1][y]:
                q.append((x-1,y))
                vis[x-1][y]=1
            dp[x-1][y]+=(dp[x][y]*(float(x)/(x+y)))
        if y:
            if not vis[x][y-1]:
                q.append((x,y-1))
                vis[x][y-1]=1
            pro=dp[x][y]*(float(y)/(x+y))
            dis=b+w-x-y
            if dis%3==0:
                #print(ans,pro,x,y-1)
                ans+=pro
            if dis%3==2:
                
                dp[x][y-1]+=(pro)
            
    print(ans)