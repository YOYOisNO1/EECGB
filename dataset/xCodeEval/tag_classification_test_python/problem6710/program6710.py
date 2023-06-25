    n = int(input())
    
    res = {}
    
    
def cal(x):
        if x == 0:
            return 0
        if x in res.keys():
            return res[x]
    
        larger = 1
        while x >= larger:
            larger = larger * 10 + 1
        smaller = larger // 10
        l = len(str(smaller))
    
        a = cal(x % smaller) + (x // smaller) * l
        b = cal((larger - x) % smaller) + l + 1 + ((larger - x) // smaller) * l
        res[x] = min(a, b)
        return res[x]
    
    
    print(cal(n))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    