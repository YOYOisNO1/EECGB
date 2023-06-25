def solve(la, ra, ta, lb, rb, tb):
        if la > lb:
            la, ra, ta, lb, rb, tb = lb, rb, tb, la, ra, ta
        da = ra-la
        db = rb-lb
        ans = 0
        dist = lb - la
        dist %= ta
        if dist == 0:
            return min(da+1, db+1)
        if tb % ta:
            dist %= ta % (tb % ta)
            la, ra = lb - dist, lb - dist + da
            ans = max(ans, 1 + min(rb, ra) - lb)
            ans = max(ans, 1 + min(rb, ra + ta % (tb % ta)) - (la + ta % (tb % ta)))
        la, ra = lb - dist, lb - dist + da
        ans = max(ans, 1+min(rb, ra) - lb)
        ans = max(ans, 1+min(rb, ra+ta) - (la+ta))
        return ans
    
    
def main():
        la, ra, ta = [int(i) for i in input().split()]
        lb, rb, tb = [int(i) for i in input().split()]
        print(solve(la, ra, ta, lb, rb, tb))
    
    
    main()