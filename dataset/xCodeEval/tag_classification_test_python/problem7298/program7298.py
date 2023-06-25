def program7298():
    m, b = map(int, input().split())
    ans = 0
    for i in xrange(b+1):
        x = m * i
        y = -1*(x / m) + b
        count = ((y+1)*(x+1)*(x+y))/2
        ans = max(count, ans)
    
    print(ans)