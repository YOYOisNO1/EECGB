    from sys import stdin
def get(n,ma):
        res = [1]
        st = 65
        if n==1:
            return res
        while st >=0:
            st-=1
            if res[-1] * n > ma:
                break
            res.append(res[-1] * n)
        return res
    try:    
        x,y,l,r = map(int,stdin.readline().split())
        a = get(x,r)
        b = get(y,r)
        c = set()
        for i in a:
            for j in b:
                if i + j >=l and i + j <=r:
                    c.add(i+j)
        c = list(c)
        c.sort()
        ans = 0
        if len(c)
            ans = max(c[0]-l,r-c[-1])
        pr = l
        for i in c:
            ans = max(ans, i-pr-1)
            pr = i
        print ans
    except:
        while True:
            n = 1