    from Queue import * # Queue, LifoQueue, PriorityQueue
    from bisect import * #bisect, insort
    from datetime import * 
    from collections import * #deque, Counter,OrderedDict,defaultdict
    import calendar
    import heapq
    import math
    import copy
    import itertools
    
def maxBy(f, x, y):
        if f(x) > f(y):
            return x
        else:
            return y
    
    table = { ("","") : "" }
    
def lcs(xs,ys):
        if (xs,ys) in table:
            return table[(xs,ys)]
    
        ret = ""
        if xs == "" or ys == "":
            ret = ""
        elif xs[-1] == ys[-1]:
            ret = lcs(xs[:-1],ys[:-1]) + xs[-1]
        else:
            ret = maxBy(len,
                        lcs(xs[:-1],ys),
                        lcs(xs,ys[:-1]))
        table[(xs,ys)] = ret
        return ret
    
def make_ans(ans, virus):
        if ans.find(virus) == -1:
            return (len(ans), ans)
    
        target = ans.find(virus)
        ans_list = []
        for i in range(len(virus)):
            new_s = ans[:target+i] + ans[target+i+1:]
            ans_list.append( make_ans(new_s, virus) )
        
        ans_list.sort(reverse = True)
        
        return ans_list[0]
    
    
def solver():
        s1 = input()
        s2 = input()
        virus = input()
       
        ans = lcs(s1,s2)
    
        
        ans = make_ans(ans, virus)[1]
        if ans == "":
            print 0
        else:
            print ans
    
    if __name__ == "__main__":
        solver()
        