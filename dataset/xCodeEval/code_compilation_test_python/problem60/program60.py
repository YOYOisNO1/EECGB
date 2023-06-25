    from collections import Counter, defaultdict, deque
    import bisect
    from sys import stdin, stdout
    from itertools import repeat
    import math
     
    # sys.stdin = open('input')
     
def inp(force_list=False):
        re = map(int, input().split())
        if len(re) == 1 and not force_list:
            return re[0]
        return re
     
def inst():
        return input().strip()
     
def gcd(x, y):
       while(y):
           x, y = y, x % y
       return x
     
    
def my_main():
        t = 1
        for _ in range(t):
            n = inp()
            k = int(math.log(n, 6))
            ans = [1] * 6
        def pro(ans):
              re = 1
              for i in ans:
                re *= i
              return re
            idx = 0
            while pro(ans) < n:
              ans[idx] += 1
              idx += 1
              
            if n<=3:
              print 'codeforces' + 's' * (n-1)
            else:
              print 'c'*ans[0] +'o'*ans[1] + 'd' + 'e'*ans[2] + 'f' + 'o'*ans[3] +'r' + 'c'*ans[4] + 'e' *ans[5] + 's'
    
    my_main()