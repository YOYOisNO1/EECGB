    from Queue import * # Queue, LifoQueue, PriorityQueue
    from bisect import * #bisect, insort
    from datetime import * 
    from collections import * #deque, Counter,OrderedDict,defaultdict
    import calendar
    import heapq
    import math
    import copy
    import itertools
    
    dp = {}
    
def long_sequence(i,j,ans_s,s2):
        if dp[(i,j)] == 0:
            return ans_s
    
    
        up = dp[(i-1,j)]
        side = dp[(i,j-1)]
        up_side = dp[(i-1,j-1)]
            
        if up == side and side == up_side and up_side ==dp[i,j] - 1:
            return long_sequence(i-1,j-1,s2[j-1]+ans_s,s2)
        elif side > up:
            return long_sequence(i,j-1,ans_s,s2)
        else:
            return long_sequence(i-1,j,ans_s,s2)        
    
    
def make_table(s1,s2,virus):
        for i in range(0,len(s1)+1):
            dp[(i,0)] = 0
        for j in range(0,len(s2)+1):
            dp[(0,j)] = 0
    
        
    
        for i in range(0,len(s1)):
            for j in range(0, len(s2)):
                l_s = long_sequence(i,j,"",s2)
                l_s += s2[j]
                if s1[i] == s2[j] and l_s.find(virus) == -1:
                    dp[(i+1,j+1)] = dp[(i,j)] + 1
                else:
                    dp[(i+1,j+1)] = max(dp[(i+1,j)],dp[(i,j+1)])
        
     
def print_dp(s1,s2):
        for i in range(0,len(s2)):
            print "%2d" % i,
    
        print len(s1)
    
        for i in range(0,len(s1)+1):
            print i,
            for j in range(0,len(s2)+1):
                print "%2d" % dp[(i,j)],
    
            print
    
def solver():
        s1 = input()
        s2 = input()
        virus = input()
       
        make_table(s1,s2,virus)
        #print_dp(s1,s2)
        ans = long_sequence(len(s1),len(s2),"",s2)
    
    
        if ans == "":
            print 0
        else:
            print ans
    
    if __name__ == "__main__":
        solver()
        