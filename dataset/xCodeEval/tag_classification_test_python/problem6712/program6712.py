def ones(a):
        return (10 ** a - 1) // 9
    
def add_in_dict(dct, key, val):
        if key in dct:
            dct[key] = min(dct[key], val)
        else:
            dct[key] = val
        
    _s = input()
    _n = len(_s)
    _x = int(_s)
    
    cur_dict = {}
    cur_dict[_x] = 0
    
    for i in range(_n + 1, 0, -1):
        ns = ones(i)
        new_dict = {}
        for x in cur_dict:
            v = cur_dict[x]
    
            while ns <= x:
                x -= ns
                v += i
    
            add_in_dict(new_dict, x, v)
            add_in_dict(new_dict, ns - x, v + i)
    
        cur_dict = new_dict
    
    print(cur_dict[0])