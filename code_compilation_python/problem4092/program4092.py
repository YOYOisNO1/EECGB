    #http://codeforces.ru/problemset/problem/255/D
    
def cells_dir(second):
        return sum(xrange(1,second*2,2))
    
def doubles(second, x, y, n):
        d = 0
        corners = [x+n-y+1, y+n-x+1, x+y, (n-x+1) + (n-y+1)]
        for corner in corners:
            if corner <= second:
                d += sum(xrange(1, second - corner + 2))
        return d
    
def cells_a(second, x, y, n):
        dcx = cells_dir(second-x+1) + cells_dir(second-n+x)
        dcy = cells_dir(second-y+1) + cells_dir(second-n+y) - doubles(second, x, y, n)
        return (sum(xrange(1,second*2,2))*2 + second*2 + 1)- dcx - dcy
    
    n, x, y, c = map(int, input().split())
    second = 0
    while cells_a(second, x, y, n) < c:
        second += 1000
    high = second
    low = second - 1000 if second !=0 else 0
    second = 0
    
    ##if c == n**2
    
    while high - low > 1:
        second = (high + low) / 2
        cells = cells_a(second, x, y, n)
        if  cells > c:
            high = second
        elif cells < c:
            low = second
        elif cells == n**2:
            high = second
        else:
            break
    else: 
        if cells_a(low, x, y, n) > c:
            second = low
        else:
            second = high
    
    print second