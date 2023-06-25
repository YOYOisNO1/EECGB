    n, l, r = map(int, input().strip().split())
    
def work(xx):
        if n == 0:
            return 0
        x = xx
        m = n
        ans = 0
        p2 = 1
        while p2 * 2 <= n:
            p2 *= 2
        while x > 0:
            if x >= p2:
                ans += (m/2) + (m%2)
                x -= p2
            p2 /= 2
            m /= 2
        return ans
    
    print(work(r)-work(l-1))