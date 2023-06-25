    import sys
    
def slist_to_int_list(l):
        return [int(x) for x  in l]
    
    
    
    first = True
    
    for line in sys.stdin:
        if first:
            n = slist_to_int_list(line.split(" "))[0]
            
            first = False
        else:
            days = slist_to_int_list(line.split(" "))
    
    
    
    #print(days)
    
    
    # 0 rest
    # 1 contest
    # 2 gym
    # 3 both
     
    last = days[0]
    
    
    if last == 0:
        res = 0
    else:
        res = 1
    
    
    for i in range(1,n):
        new = days[i]
        #print(last,) new,res
        if last == 0 and not new == 0:
            res +=1
            last = new
        elif last == 1 and new == 1:
            last = 0
        elif last == 3 and not new == 0:
            last = new
            res += 1
        elif last == 2 and new == 2:
            last = 0
        elif new == 3 and last == 1:
            last = 2
            res +=1
        elif new == 3 and last == 2:
            last = 1
            res +=1
        elif new == 0:
            last = 0
        else:
            # gym and contest or contrary
            last = new
            res += 1
    
    
    print(n-res)
        
    