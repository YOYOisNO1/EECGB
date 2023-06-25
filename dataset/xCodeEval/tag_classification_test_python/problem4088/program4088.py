    # import tensorflow as tf
    
    
def process(n, k):
        res = 0
        #  print(n,) k
        t = n
        while t > 0:
            p_count = min(t, k)
            res += p_count
            t -= p_count
            v_count = t / 10
            t -= v_count
            #  print(p_count,) v_count, n, res
        return res >= (n + 1) / 2
    
    
def solve(n):
        l, r = 0, n
        while r - l > 1:
            m = (r + l) / 2
            if process(n, m):
                r = m
            else:
                l = m
        #  print(r)
        return r
    
    
def test():
        assert solve(68) == 3
        assert solve(1) == 1
        assert solve(10) == 1
    
    if __name__ == '__main__':
        test()
        n = int(input())
        print(solve(n))