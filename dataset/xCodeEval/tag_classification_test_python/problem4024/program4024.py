    w,m = map(int,input().split())
    
def solve(m,curw):
        cursum = 0
        if m==0 : return 1
        for i in range(curw):
            cursum += w**i
            if cursum==m : return 1
            if cursum>m or w**i==m: return solve(abs(w**i-m),i)
        return 0
    
    print('YES' if solve(m,100) else 'NO')
            
    
    