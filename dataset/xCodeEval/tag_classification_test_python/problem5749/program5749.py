    from Queue import * # Queue, LifoQueue, PriorityQueue
    from bisect import * #bisect, insort
    from datetime import * 
    from collections import * #deque, Counter,OrderedDict,defaultdict
    from sets import * #Set
    import calendar
    import heapq
    import math
    import copy
    import itertools
    myread = lambda : map(int,input().split())
    
def min_frac(now_min,ans,k,x,y):
        a,b = now_min
        if k * abs(b * x - a * y) > b * abs(k * x - ans * y):
            return [ans,k]
        else:
            return now_min
def solver():
        x,y,n = myread()
        now_min = [10000000,1]
        for k in range(1,n+1):
            ans1 = k * x / y
            ans2 = (k * x) / y + 1
            #print(ans1,ans2)
            now_min = min_frac(now_min,ans1,k,x,y)
            now_min = min_frac(now_min,ans2,k,x,y)
        print(str(now_min[0])) + "/" + str(now_min[1])
    if __name__ == "__main__":
        solver()
        