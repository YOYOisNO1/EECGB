def program7296():
    # Time   : 2017-6-26 13:30
    # Auther : Anjone
    # URL : http://codeforces.com/contest/821/problem/B
    
    from math import floor;
    getsum = lambda x,y : ( y + 1 ) * ( x + y ) * (x+1) // 2
    
    m,b = map(int,input().split())
    ans = 0
    for i in range(b+1):
    	ans = max(ans, getsum( ( b - i ) * m, i))
    print(ans)