    import sys
    
    # inf = open('input.txt', 'r')
    # reader = (map(int, line.split()) for line in inf)
    reader = (map(int, line.split()) for line in sys.stdin)
    
def count(num):
        ans = 0
        if num % 2:
            add = 1
        else:
            add = 2
        while num + add - 1 <= n:
            ans += add
            add *= 2
            num *= 2
        if num <= n:
            ans += n - num + 1
        return ans
    
def func(n, k):
        if k == n:
            return 1
        # odd
        L = 0
        R = n // 2 + n % 2
        while L + 1 < R:
            m = (L + R) // 2
            num = 2 * m + 1
    #         print(num, count(num))
            if count(num) >= k:
                L = m
            else:
                R = m
        m_odd = 2 * L + 1
        
        # even
        L = 1
        R = n // 2 + 1
        while L + 1 < R:
            m = (L + R) // 2
            num = 2 * m
    #         print(num, count(num))
            if count(num) >= k:
                L = m
            else:
                R = m
        m_even = 2 * L
        return max(m_odd, m_even)
        
    n, k = next(reader)
    ans = func(n, k)
    print(ans)
    
    # inf.close()