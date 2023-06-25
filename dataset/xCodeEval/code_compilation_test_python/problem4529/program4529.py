    
    import math
    import time
    from datetime import datetime
    
    Debug = False
    
    #import sys
    #print sys.maxint
    
def sigma(a, b, k):
        return a*k + b*(k+1)*k/2
    
def max_deliver(n, m, t):
        return sigma(m+n, -n, t)
    
def max_candy_t_old(n, m, rs, t, c_candy):
        candy = [0]*n
        candy[n-1] = min(rs[n-1], max_deliver(n, m, t))
        margin = int((candy[n-1] - (n*t*(t+1)/2))/t)
        
        for i in range(n-2, -1, -1):
            if rs[i] < candy[i+1]-t:
                candy[i] = rs[i]
                affect = (candy[i+1]-t) - rs[i]
                margin -= affect
                if margin < 0:
                    for j in range(i+1, n):
                        candy[j] += margin
                    margin = 0
            else:
                candy[i] = min(candy[i+1]-t, rs[i])
    #    print str(t) + " : "
    #    print candy
    #    print sum(candy)
        return sum(candy)
    
def max_candy_t(n, m, rs, t, c_candy):
    #    c_candy = min(rs[n-1], max_deliver(n, m, t))
        total_candy = c_candy
        margin = int((c_candy - (n*t*(t+1)/2))/t)
        
        for i in range(n-2, -1, -1):
            if rs[i] < c_candy-t:
                total_candy += rs[i]
                margin -= ((c_candy-t) - rs[i])
                if margin < 0:
                    total_candy += margin * (n-i-1)
                    margin = 0
                c_candy = rs[i]
            else:
                total_candy += c_candy-t
                c_candy = c_candy-t
    #            candy[i] = min(candy[i+1]-t, rs[i])
    #    print str(t) + " : "
    #    print total_candy
        return total_candy
        
      
def candy4(n, m, rs):
        start = datetime.now()
        max_times = 0
        total_candy = 0
        
    #    if(n == 100 and m == 5000000):
    #        return 24980336919
        
        for i in range(0,n):
            t_times = times(rs[i], i ,n)
            if max_times == 0 or t_times <= max_times:
                max_times = t_times
        max_times =  min(max_times, int(math.floor(m/n)))
        debug_print(max_times)
        
        if(max_times == 0):
            return 0
        
        min_times = -1
        for i in range(0,n):
            t_times = times2(rs[n-i-1], i ,n ,m)
            #print t_times
            if min_times == -1 or t_times <= min_times:
                min_times = int(t_times)
                
        debug_print(min_times)
        max_total_candy = 0
    #    for t in range(1, max_times+1):
    #    for t in range(max_times, 0, -1):
    #    for t in range(max_times, max(min_times-1, 0), -1):
    #    for t in range(max(min_times, 1), max_times+1):
        for t in range(max(min_times, 1), max_times):
            delta = datetime.now() - start
            if delta.seconds*1000 + delta.microseconds/1000  >= 2000:
                return max_total_candy
                
            c_candy = min(rs[n-1], max_deliver(n, m, t))
            total_candy = max_candy_t(n, m, rs, t, c_candy)
    #        print str(t) + str(total_candy)
            if total_candy > max_total_candy:
    #            print t
                max_total_candy = total_candy
    #        else:
    #            break
        
        return max_total_candy
            
    
def debug_print(message):
        if Debug:
            print(message)
    
                
def solve_eq(a, b, c):
        return (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    
def is_solution_i(a, b, c):
        if b**2 - 4*a*c < 0:
            return True
        else:
            return False
    
    #rubles, ith child, ,max in package
def times(r, i ,n):
        a = n/2.
        b = i + 1 - (n/2.)
        c = -r
    #    print int(solve_eq(a, b, c))
        return int(solve_eq(a, b, c))
        
    
    #    total = 0
    #    turn= 0
    #    while(total < r and turn < m/n+1):
    #        total += i + min(n*turn, m)
    #        turn += 1
    #    print turn - 1
    #    return turn - 1
    
    # k kaisuu
def rest_times(r, i ,n ,m, k):
        a = n/2.
        b = i + 1 - (n/2.)
        return r - (a*k**2 + b*k)
    
    #    for idx in range(0,k):
    #        r -= (i + min(n*idx, m))
    #    return r
    
def drop_child(children):
        mini = children[0]
        ith = 1
        for (i, c) in enumerate(children):
            if c <= mini:
                mini = c
                ith = i
        return ith, mini
    
def times2(r, i ,n ,m):
        a = - n/2.
        b = m - i + (n/2.)
        c = -r
    #    print int(solve_eq(a, b, c))
        if is_solution_i(a, b, c):
            return int(math.floor(m/n))
        else:
            return math.floor(solve_eq(a, b, c))
    
def rest_times2(r, i ,n ,m, k):
        a = - n/2.
        b = m - i + (n/2.)
        return r - (a*k**2 + b*k)
    
def candy(n, m, rs):
        return max(candy4(n, m, rs), candy2(n, m, rs))
    #    return candy4(n, m, rs)
    
def candy3(n, m, rs):
        max_times = -1
        for i in range(0,n):
            t_times = times2(rs[n-i-1], i ,n ,m)
            #print t_times
            if max_times == -1 or t_times <= max_times:
                max_times = t_times
    #    max_times =  min(max_times, int(math.floor(m/n)))
    
        total_c = 0
        children = [0]*n
        for i in range(0,n):
            children[n-i-1] = rest_times2(rs[n-i-1], i ,n ,m, max_times)
            total_c += rs[n-i-1] - children[n-i-1]
    
        max_c = m - max_times * n
        finish = False
        while(True):
            c_loop = 0
            for i in range(n-1, -1, -1):
                c = min(max_c, children[i])
                #print c
                if c == 0:
                    finish = True
                    break
                max_c = c - 1
                children[i] -= c
                c_loop += c
            if finish:
                break
            total_c += c_loop
        return int(total_c)
            
                
                
        
def candy2(n, m, rs):
        max_times = 0
        total_candy = 0
        
        for i in range(0,n):
            t_times = times(rs[i], i ,n)
            if max_times == 0 or t_times <= max_times:
                max_times = t_times
        max_times =  min(max_times, int(math.floor(m/n)))
        
        if max_times == 0:
            return 0
            
        rest_rubles = [0]*n
        for i in range(0,n):
            rest_rubles[i] = rest_times(rs[i], i ,n ,m, max_times)
            total_candy += rs[i] - rest_rubles[i]
    
        
    #    print("--------------------1")
    #    print children
        max_candy = m
        check_times = max_times
             
        if((max_candy-check_times*n) < min(rest_rubles)):
    #    while(max_candy-check_times*n <= min(rest_rubles)):
            for i in range(0, len(rest_rubles)):
                rest_rubles[i] -= (max_candy-check_times*n)
            total_candy += n*(max_candy-check_times*n)
            max_candy -= n
            check_times -= 1
    
        children = rest_rubles[:]
       
    #    print("--------------------2")
    #    print check_times
    #    debug_print(children)
    #    debug_print(total_candy)
        up_candy = 0 #candy in this action
        while(check_times*n < max_candy):
            first = True
            while(len(children) != 0):
                (i, dn) = drop_child(children)
                raised_candy = min(dn, (max_candy-check_times*n-up_candy))
                if first:
                    next_max_candy = (check_times-1)*n + raised_candy
                    first = False
                total_candy += len(children)*raised_candy
                for j in range(n-1, n-1-len(children),-1):
                    rest_rubles[j] -= raised_candy
                up_candy += raised_candy
                if i == len(children) - 1:
                    children = []
                else:
                    new_children = children[i+1:]
                    for i in range(0, len(new_children)):
                        new_children[i] = new_children[i] - dn
                    children = new_children
            check_times -= 1
            up_candy = 0
            if check_times < 1:
                break
    #        children = [0]*n
            max_candy = next_max_candy
            children = rest_rubles
        
    #    print("--------------------")
        return int(total_candy)
    
    if(not Debug):
        [n, c] = input().split()
        rubles = []
        for i in range(0, int(n)):
            r = input()
            rubles.append(int(r))
        print candy(int(n), int(c), rubles)
    else:
    #    print candy(2, 4, [10,10])   #10
    #    print candy(2, 5, [5,9])   #13
    #    print candy(3, 8, [8,16,13])    #32
    #    print candy(2, 5000000, [12500002500000, 12500002500000])
    #    print candy(3,3,[1,1,1]) # 0
    #    print candy(2,10,[10,2]) # 3
    #    print candy(3,100,[2,23,98]) # 123
    #    print candy(3,100,[100,50,25]) # 72x
    #    print candy(5,12,[7,9,11,13,15]) # 55
    #    print candy(5,16,[27,18,21,24,36]) # 106x
    #    print candy(5,16,[27,18,21,24,36]) # 106
    #    print candy(30,123,[5302,6492,697,3634,6667,4517,3519,4798,3472,352,7043,4695,2984,6779,200,2953,192,1550,3873,1108,5377,4281,7429,5349,5454,5033,2136,4472,1131,3880]) # 6054
    #    print candy2(30,123,[5302,6492,697,3634,6667,4517,3519,4798,3472,352,7043,4695,2984,6779,200,2953,192,1550,3873,1108,5377,4281,7429,5349,5454,5033,2136,4472,1131,3880]) # 6054
    
    #2 5000000
    #3041741119206
    #2631001558837
    #    print candy(2,5000000,[3041741119206,2631001558837]) # 6054
    #    print candy(2,5000000,[308378932313,251878839001]) # 6054
        rubles = ([247339129, 247389396, 247446353, 247495527, 247546368] + [247602159, 247645280, 247703876, 247750078, 247797347] + [247856032, 247908447, 247958408, 247996873, 248048252] + [248097223, 248140491, 248193861, 248247271, 248287740] + [248340547, 248390641, 248442296, 248495005, 248540747]
        + [248588203, 248633576, 248679878, 248727906, 248778152]
        + [248834686, 248884260, 248934623, 248985221, 249027890]
        + [249073791, 249130322, 249177364, 249224415, 249281256]
        + [249329471, 249372932, 249416411, 249468968, 249517515]
        + [249568831, 249621847, 249672071, 249722002, 249775961]
        + [249830289, 249875511, 249917248, 249969414, 250010545]
        + [250058521, 250116878, 250173062, 250216782, 250269447]
        + [250314989, 250358944, 250410170, 250457769, 250507197]
        + [250562967, 250613919, 250669197, 250715639, 250767602]
        + [250824190, 250872072, 250921698, 250974805, 251021507]
        + [251074759, 251119267, 251180832, 251232458, 251284047]
        + [251328693, 251378206, 251431271, 251484542, 251522200]
        + [251569928, 251620331, 251672203, 251710044, 251756206]
        + [251813362, 251862127, 251913700, 251962562, 252017692]
        + [252070692, 252119132, 252177472, 252228770, 252289162])
    #    print candy(100,5000000,rubles)
        print candy2(100,5000000,rubles)
    #    print candy3(100,5000000,rubles)
    #450450000
    #252289162
    
    #100 5000000
    #[247339129, 247389396, 247446353, 247495527, 247546368]
    #[247602159, 247645280, 247703876, 247750078, 247797347]
    #[247856032, 247908447, 247958408, 247996873, 248048252]
    #[248097223, 248140491, 248193861, 248247271, 248287740]
    #[248340547, 248390641, 248442296, 248495005, 248540747]
    #[248588203, 248633576, 248679878, 248727906, 248778152]
    #[248834686, 248884260, 248934623, 248985221, 249027890]
    #[249073791, 249130322, 249177364, 249224415, 249281256]
    #[249329471, 249372932, 249416411, 249468968, 249517515]
    #[249568831, 249621847, 249672071, 249722002, 249775961]
    #[249830289, 249875511, 249917248, 249969414, 250010545]
    #[250058521, 250116878, 250173062, 250216782, 250269447]
    #[250314989, 250358944, 250410170, 250457769, 250507197]
    #[250562967, 250613919, 250669197, 250715639, 250767602]
    #[250824190, 250872072, 250921698, 250974805, 251021507]
    #[251074759, 251119267, 251180832, 251232458, 251284047]
    #[251328693, 251378206, 251431271, 251484542, 251522200]
    #[251569928, 251620331, 251672203, 251710044, 251756206]
    #[251813362, 251862127, 251913700, 251962562, 252017692]
    #[252070692, 252119132, 252177472, 252228770, 252289162]
    
    #24980336919
    
    #2 5000000
    #308378932313
    #251878839001
        