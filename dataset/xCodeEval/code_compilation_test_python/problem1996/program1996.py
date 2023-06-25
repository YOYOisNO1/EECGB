    from sys import stdin
    import sys
    #sys.setrecursionlimit(1500)
    input = stdin.readline
    
def dp(curStage, curK, firstK, n, l, k):
        
        
        if curStage == n:
            return True
        
        nextK = (curK + 1) % (2 * k)
        
        
        if nextK >= k:
            nextLevelWait = d[curStage] + ((2 * k) - nextK)
            nextLevelGo = d[curStage + 1] + ((2 * k) - nextK)
        else:
            nextLevelWait = d[curStage] + nextK
            nextLevelGo = d[curStage + 1] + nextK
    
    
        #print(curStage, curK, nextK, nextLevelGo, nextLevelWait)
        
        a = False
        b = False
        if nextLevelGo <= l:
            a = dp(curStage + 1, nextK, nextK, n, l, k)
        if a:
            return a
        if nextLevelWait <= l and nextK != firstK:
            b = dp(curStage, nextK, firstK, n, l, k)
        if b:
            return b
    
    t = int(input())
    
    for _ in range(t):
        
        n, k, l = list(map(int, input().rstrip().split(" ")))
        d = list(map(int, input().rstrip().split(" ")))
        d.insert(0, -999)
       
        
        if dp(0, 0, 0, n, l, k):
            print('Yes')
        else:
            print('No')
        
    
        
           
                
                
                