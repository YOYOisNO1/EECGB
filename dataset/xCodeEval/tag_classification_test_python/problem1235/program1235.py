    from itertools import combinations
    
    f,r, c = list(map(int, input().split()))
    count = 0
    maxi = min(f//3, r//2, c//2)
    
    f -= 3*maxi
    r -= 2*maxi
    c -= 2*maxi
    count += maxi*7
    week = "0120210"
    week = week
    #some f r c
def check(n,some, c):
    
        if c >= 7:
            return c
        if some[int(week[n])] > 0:
            some[int(week[n])] -= 1
        else:
            return c
        return check(n+1, some, c+1)
    
    
    
    
    maxi_co = 0
    for i in range(7):
        this = [f, r, c]
        co = 0
        new = week[i:]+week[:i+1]
        # print(new)
        for i in new:
            if this[int(i)] == 0:
                break
            else:
                this[int(i)] -= 1
                co += 1
        maxi_co = max(maxi_co, co)
    
    print(count+maxi_co)