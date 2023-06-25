def judge(x):
        w, d = divmod(x, 7)
        a2 = 3*w+l[:d].count('a')
        b2 = 2*w+l[:d].count('b')
        c2 = 2*w+l[:d].count('c')
        
        return a>=a2 and b>=b2 and c>=c2
    
def binary_search():
        l, r = 0, 10**10
        
        while l<=r:
            mid = (l+r)//2
            
            if judge(mid):
                l = mid+1
            else:
                r = mid-1
        
        return r
    
    a, b, c = map(int, input().split())
    l = list('abcacba')
    ans = 0
    
    for _ in range(7):
        ans = max(ans, binary_search())
        l = l[1:]+[l[0]]
    
    print(ans)