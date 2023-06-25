    #     Clever Fat Rat
    import time
    from datetime import datetime
    
def is_goal(state):
        (a, ws) = state
        if(len(ws) == 1 and ws[0][0] <= a[0]):
            return True
    
def child(state):
        (a, ws) = state 
        scales = ws[0]
        if(len(ws) == 1):
            return [];
        
        b = [[0]*(len(scales)-1)]
        for (jdx, scale) in enumerate(scales):
            if a[jdx] >= scale:
                if(jdx == 0):
                    b = map(lambda x: [x[0]+a[jdx]] + x[1:], b)
    #                b[0] += a[jdx]
                elif (jdx == len(scales)-1):
                    b = map(lambda x:  x[:-1]+[x[-1]+a[-1]], b)
    #                b[-1] += a[-1]
                else:
                    b = map(lambda x:  [x[:jdx]+[x[jdx]+a[jdx]]+x[jdx+1:], x[:jdx-1]+[x[jdx-1]+a[jdx]]+x[jdx:]], b)
                    b = reduce (lambda a,b: a+b, b)
    #                b[jdx-1] += a[jdx]/2.
    #                b[jdx] += a[jdx]/2.
    #    print b
        return map(lambda x: (x, ws[1:]), b)
        
def is_possible_reach_goal(state):
    #    print state
        (a, ws) = state
        return (sum(a) >= ws[-1][0])
    
def is_broken(i, a, ws):
        return 1 if (a[i] >= ws[0][i]) else 0
    
def fall(idx, a, ws):
        return a[idx]  * is_broken(idx, a, ws)
    
def check_break(a, ws):
        break_list = [[0,0]]
        for idx in range(0, len(a)-1):
            break_list += [[0,0]]
            if(fall(idx, a, ws) + fall(idx+1, a, ws) >= ws[1][idx]):
                break_list[idx][1] = is_broken(idx, a, ws)
                break_list[idx+1][0] = is_broken(idx+1, a, ws)
        return break_list
    
def next_step(a, break_list):
        next_step = [[]]
        for idx, b in enumerate(break_list):
            if b == [0,0]:
                next_step = map((lambda x: x+[0]), next_step)
            elif b == [0,1]:
                next_step = map((lambda x: x+[a[idx]]), next_step)
            elif b == [1,0]:
                next_step = map((lambda x: x[:-1] + [x[-1]+a[idx]] +[0]), next_step)
            else:   # [1,1]
                next_step = map((lambda x: [x[:-1] + [x[-1]+a[idx]] +[0], x+[a[idx]]]), next_step)
                next_step = reduce (lambda a,b: a+b, next_step)
        return map(lambda x: x[:-1],next_step)
                    
    
def fatrat(state):
    #    print state
        (a, ws) = state
    
        a_list = [a]
        while(True):
            if len(ws) == 1:
                for e_a_list in a_list:
                    if e_a_list[0] >= ws[0][0]:
                        return "Cerealguy"
                return "Fat Rat"
            
            a_list = map((lambda a: next_step(a, check_break(a, ws))), a_list)
            a_list = reduce (lambda a,b: a+b, a_list)
            
            new_list = []
            for e_a_list in a_list:
                if e_a_list not in new_list:
                    if sum(e_a_list) >= ws[-1][0]:
                        new_list.append(e_a_list)
                    
            a_list = new_list
            ws = ws[1:]
            
            if not len(a_list):
                return "Fat Rat"
                
            
    
    
def fatrat2(state):
        stack = [state]
        visited = []
        start = datetime.now()
        
        while(stack):
    
            state = stack.pop()
            visited += [state[0]]
            
            if(is_goal(state)):
                return "Cerealguy"
            
            children = child(state)
            for c in children:
                if(c[0] not in visited and c not in stack):
                    if is_possible_reach_goal(c):
                        stack += [c]
       
        return "Fat Rat" 
        
    
        
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
    #    print fatrat(n, a, ws)
        print fatrat(((a, ws)))
    else:
    #    print fatrat(([1], [[2]]))   #F
    #    print fatrat(([2, 2], [[1, 2],[4]]))   #C
    #    print fatrat(([2, 2], [[1, 2],[5]]))   #F
    #    print fatrat(([798097, 886901, 292688, 792934], [[987579, 447910, 689959, 311317],[41624, 797440, 706737],[921438, 988902],[506461]]))   #C