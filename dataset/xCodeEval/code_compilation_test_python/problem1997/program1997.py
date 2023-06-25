    from sys import stdin
    import sys
    sys.setrecursionlimit(1500)
    input = stdin.readline
    
    
    
    
    
    
def dp(curStage, curK, firstK, n, l, k, results):
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
            if (curStage + 1, nextK) in results:
                a = False
            else:
                a = dp(curStage + 1, nextK, nextK, n, l, k, results)
                if not a:
                    results.add(a)
        if a:
            return a
        
        if nextLevelWait <= l and nextK != firstK:
            if (curStage, nextK) in results:
                b = False
            else:
                b = dp(curStage, nextK, firstK, n, l, k, results)
                if not b:
                    results.add(b)
                
        if b:
            return b
    
    t = int(input())
    
    for _ in range(t):
        
        n, k, l = list(map(int, input().rstrip().split(" ")))
        d2 = list(map(int, input().rstrip().split(" ")))
        d = [-999]
        d.extend(d2)
       
        r = set()
        if dp(0, 0, 0, n, l, k, r):
            print('Yes')
        else:
            print('No')
        
    
        
           
                
                
                