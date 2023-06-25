    from Queue import * # Queue, LifoQueue, PriorityQueue
    from bisect import * #bisect, insort
    from datetime import * 
    from collections import * #deque, Counter,OrderedDict,defaultdict
    import calendar
    import heapq
    import math
    import copy
    import itertools
    myread = lambda : map(int,input().split())
    
def OK(n,m,w,k):
        max_num = n + m - 1
        len_m = len(str(m))
        len_max = len(str(max_num))
    
        if len_m == len_max:
            ans = ((max_num - m) + 1) * len_m * k
        else:
            ans = ((10 ** (len_m) - m)) * len_m * k
            for i in range(len_m,len_max-1):
                ans += 9 * (10 ** i) * (i+1) * k
                
            ans += (max_num - (10 ** (len_max - 1)) + 1) * len_max * k
    
        return ans <= w
        
    
    
def solver():
        w,m,k = input().split()
        w = int(w)
        k = int(k)
        m = int(m)
    
        lp = 0
        up = 10 ** 16 + 100
    
        while lp != up:
            mid = (lp + up) / 2 + 1
            
            if OK(mid,m,w,k):
                lp = mid
            else:
                up = mid - 1
            
    
        print(lp)
    
        
    
    
    
    
    
    
    
    
    
    if __name__ == "__main__":
        solver()
        