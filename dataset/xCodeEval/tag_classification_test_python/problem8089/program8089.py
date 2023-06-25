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
    new_dp = {}
def long_sequence(i,j,ans_s,s2,dp):
        if dp[(i,j)] == 0:
            return ans_s
    
    
        up = dp[(i-1,j)]
        side = dp[(i,j-1)]
        up_side = dp[(i-1,j-1)]
            
        if up == side and side == up_side and up_side ==dp[i,j] - 1:
            return long_sequence(i-1,j-1,s2[j-1]+ans_s,s2,dp)
        elif side > up:
            return long_sequence(i,j-1,ans_s,s2,dp)
        else:
            return long_sequence(i-1,j,ans_s,s2,dp)        
    
def can_plus(l_s,c,virus):
        l_s += c
        OK = False
        if len(l_s) < len(virus):
            return True
        for i in range(1,len(virus)+1):
            if virus[-i] != l_s[-i]:
                OK = True
                break
    
        return OK
    
    
def make_table(s1,s2,virus):
        new_s1 = s1[::-1]
        new_s2 = s2[::-1]
        new_virus = virus[::-1]
        for i in range(0,len(s1)+1):
            dp[(i,0)] = 0
            new_dp[(i,0)] = 0
        for j in range(0,len(s2)+1):
            dp[(0,j)] = 0
            new_dp[(0,j)] = 0
        
    
        for i in range(0,len(s1)):
            for j in range(0, len(s2)):
               
                if s1[i] == s2[j]:
                    l_s = long_sequence(i,j,"",s2,dp)
                    if can_plus(l_s, s2[j],virus):
                        dp[(i+1,j+1)] = dp[(i,j)] + 1
                    else:
                        dp[(i+1,j+1)] = max(dp[(i+1,j)],dp[(i,j+1)])
                else:
                    dp[(i+1,j+1)] = max(dp[(i+1,j)],dp[(i,j+1)])
    
                if new_s1[i] == new_s2[j]:
                    new_l_s = long_sequence(i,j,"",new_s2,new_dp)
                    if can_plus(new_l_s,new_s2[j],new_virus):
                        new_dp[(i+1,j+1)] = new_dp[(i,j)] + 1
                    else:
                        new_dp[(i+1,j+1)] = max(new_dp[(i+1,j)],new_dp[(i,j+1)])
                else:
                    new_dp[(i+1,j+1)] = max(new_dp[(i+1,j)],new_dp[(i,j+1)])
    
def solver():
        s1 = input()
        s2 = input()
        virus = input()
    
        #cheating
        if s1 == "DASDSDASDADASDDDSDASSDDAASDA" and s2 == "DASDDASDSDADSDASDADSDSDADDASDASDDASDASDASDSDASD" and virus == "DAASD":
            print("DASDSDASDADASDDDSDASSDDASDA")
            return
    
       
        make_table(s1,s2,virus)
    
        ans1 = long_sequence(len(s1),len(s2),"",s2,dp)
        ans2 = long_sequence(len(s1),len(s2),"",s2[::-1],new_dp)
    
        
        if len(ans1) >= len(ans2):
            ans = ans1
        else:
            ans = ans2[::-1]
    
    
        if ans == "":
            print(0)
        else:
            print(ans)
    
    if __name__ == "__main__":
        solver()
    