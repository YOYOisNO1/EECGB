    #     Clever Fat Rat
    import time
    from datetime import datetime
    
    import itertools
    
    max_oats = 10**6 + 1
            
def weight(p):
        return p[0]
    
def right(p):
        return p[1][1]
    
def left(p):
        return p[1][0]
    
def plus(l, r):
        return (weight(l)+weight(r), (left(l), right(r)))
    
    # 01 can cover 02?
def cover(o1, o2):
        return left(o1) >= left(o2) and right(o1) <= right(o2) and weight(o1) >= weight(o2)
    
def add_only_unique(oats, oat):
        for idx, o_n in enumerate(oats):
            if oat == o_n or cover(o_n, oat):
                return oats
            if cover(oat, o_n):
                oats[idx] = oat
                return oats
        oats.append(oat)
        return oats
    
def max_drop(oats):
        max_drop = 0
        for oat in oats:
            max_drop = weight(oat) if  weight(oat) > max_drop else max_drop
        return max_drop
    
def possible_oats(a, ws):
        oats_list = []
        for idx in range(0, len(a)-1):  # same as len(ws)
            oats = []
            left_oat = a[idx]
            right_only_oat = [e for e in a[idx+1] if not e in left_oat ]
            left_only_oat = [e for e in a[idx] if not e in a[idx+1] ]
    
            if ((len(a[idx+1]) == 0) or
                (idx != len(a)-2 and max_drop(a[idx+1])+max_drop(a[idx+2]) >= ws[0][idx+1])):
                for l in left_oat:
                    if weight(l) >= ws[0][idx]:
                        oats.append(l)
                            
            if ((len(a[idx]) == 0) or
                (idx != 0 and len(oats_list[-1]) != 0)):
                for r in right_only_oat:
                    if weight(r) >= ws[0][idx]:
                        oats = add_only_unique(oats, r)
            
            for c in itertools.product(left_only_oat,right_only_oat):
                (l,r) = c
                if weight(r)+weight(l) >= ws[0][idx] and right(l) < left(r):
                    oats = add_only_unique(oats, plus(l,r))
    
            if len(oats) > 30:
                oats.sort(key=weight, reverse=True) 
                oats = oats[:30]
            oats_list.append(oats)   
        return oats_list
                    
def is_break_all(limit, oats_list):
        for idx, oat in enumerate(oats_list):
            for o in oat:
                if weight(o) >= limit[idx]:
                    return True
        return False
        
def fatrat(state):
    #    print state
    
        (a, ws) = state
        ws = map(lambda x: [max_oats]+x+[max_oats], ws)
    
        goal_oats = []
        pre_goal_oat = [0, 0]
        for idx in range(len(ws)-1,-1,-1):
            goal_oat = []
            for jdx in range(1,len(ws[idx])-1):
                goal_oat.append(max(ws[idx][jdx],min(pre_goal_oat[jdx-1], pre_goal_oat[jdx])))
            goal_oats.append(goal_oat)
            pre_goal_oat = [max_oats] + goal_oat + [max_oats]
        goal_oats.reverse()
        ws = map(lambda x: x[1:-1], ws)
    
        oats_list = []
        for idx in range(0, len(a)):
            if a[idx] >= ws[0][idx]:
                oats_list.append([(a[idx], (idx,idx))])
            else:
                oats_list.append([])
        
        while(True):
            ws = ws[1:]
            if not len(ws):
                if len(oats_list[0]):
                    return "Cerealguy"
                else:
                    return "Fat Rat"
                
            if is_break_all(goal_oats[0], oats_list):
                return "Cerealguy"
                
            oats_list = possible_oats(oats_list, ws)
            goal_oats = goal_oats[1:]
                            
                                 
def create_goals(ws):
        ws = map(lambda x: [max_oats]+x+[max_oats], ws)
    
        goal_oats = []
        pre_goal_oat = [0, 0]
        for idx in range(len(ws)-1,-1,-1):
            goal_oat = []
            for jdx in range(1,len(ws[idx])-1):
                goal_oat.append(max(ws[idx][jdx],min(pre_goal_oat[jdx-1], pre_goal_oat[jdx])))
            goal_oats.append(goal_oat)
            pre_goal_oat = [max_oats] + goal_oat + [max_oats]
        goal_oats.reverse()
    #    ws = map(lambda x: x[1:-1], ws)
        return goal_oats
    #    print goal_oats
    
def compare_goal(goals, oats):
        for idx in range(0,len(goals)):
            if(goals[idx] <= oats[idx]):
                return True
        return False
        
    Debug = False
    if(not Debug):
        n = int(input())
        a_s = input().split()
        a = []
        for a_s_e in a_s:
            a += [int(a_s_e)]
        
        ws = []
        for i in range(0, int(n)):
            r = input().split()
            rs = []
            for e_rs in r:
                rs += [int(e_rs)]
            ws += [rs]
        print fatrat(((a, ws)))
    else:
        worst_w = [[50]]
        for idx in range(1,50):
            worst_w.append([1]*(idx+1))
        worst_w.reverse()
    #    print fatrat(([1]*50, worst_w))   #F
     
        assert fatrat(([1,1,1,1,1,1,1],[[1,9,1,9,1,9,9],[1,9,1,9,1,9],[1,1,9,1,9],[1,9,9,1],[1,9,1],[1,1],[3]])) == "Cerealguy"
        assert fatrat(([1, 1, 2, 2, 1, 1], [[1, 1, 2, 2, 1, 1],[2, 4, 2, 4, 2],[2,2,2,2],[4,10,4],[4,4],[8]])) == "Fat Rat"
        assert fatrat(([1, 1, 1], [[1, 1, 1],[1, 1],[4]])) == "Fat Rat"  #F
        assert fatrat(([2, 2, 2], [[2, 2, 2],[3, 2],[4]])) == "Cerealguy"  #C
        assert fatrat(([1], [[1]])) == "Cerealguy" #C
        assert fatrat(([2, 2], [[1, 2],[4]])) == "Cerealguy"   #C
        assert fatrat(([2, 2], [[1, 2],[5]])) == "Fat Rat"  #F
        print "great!"
    
    