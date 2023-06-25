    # -*- coding:utf8 -*-
    # by utoppia
    # 09-05-2019
    
    n, m = map(int, input().split(' '))
    
def f(n, m):
        ans = 1
        if m == 0 :
            return  1
        if m == 1:
            if n > 1:
                return 1
            else:
                return  0
        
    
        if m >= 2:
            m -= 2
            n -= 3
    
        if n <= -1:
            ans = 0
        else:
            p = 1
            left = n
            while m > 0:
                m -= 1
                if left >= 2:
                    p += 1
                    left -= 2
                    if left == 1:
                        p += 1
                        left = 0
                else:
                    p -= 1
            ans = p 
            if left:
                ans += 1
        return ans
    
    print(f(n,) m)