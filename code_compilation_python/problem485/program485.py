    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Wed Nov 23 19:21:19 2016
    
    @author: kostiantyn.omelianchuk
    """
    
    
    import math
    
    #n, a, b, c = 3164, 42, 430, 1309
    
    #n = 3119
    #a = 3515
    #b = 1021
    #c = 7
    
    
    
def sort_by_value(a,b,c):
        lowest = min(a,b,c)
        biggest = max(a,b,c)
        average = a + b + c - lowest - biggest
        return lowest,average,biggest
        
    
    
def get_max_ribbons(n,a,b,c):
        if n == 0:
            return 0
        a1,b1,c1 = sort_by_value(a,b,c)
        a_ribbons = 0
        b_ribbons = 0
        c_ribbons = 0
        if a1 == 0:
            return 'error'
        rest = n%a1
        a_ribbons = math.floor(n/a1)
        if rest == 0:
            return a_ribbons
        else:
            for i in range(1,math.floor(n/a1)):
                #print(a_ribbons, b_ribbons, c_ribbons, rest)
                a_ribbons -= 1
    #            if a_ribbons < 0:
    #                a_ribbons = 0
                rest += a1
                if b1<=rest:
                    b_ribbons += 1
                    rest = n - (a_ribbons * a1 + b_ribbons * b1 + c_ribbons * c1)
                if rest == 0:
                    #print('succes1')
                    return a_ribbons + b_ribbons + c_ribbons
                else:
                    if b_ribbons>0:
                        for j in range(1, b_ribbons):
                            if c1<=(rest+b1*j):
                                #print("here: ", a_ribbons, b_ribbons, c_ribbons, rest)
                                b_ribbons -= j
                                rest += j*b1
                                c_ribbons += 1
                                rest = n - (a_ribbons * a1 + b_ribbons * b1 + c_ribbons * c1)
                                if rest == 0:
                                #print('succes2')
                                    return a_ribbons + b_ribbons + c_ribbons
            if rest != 0:
                if n%b1 == 0:
                    return math.floor(n/b1)
                if n%c1 == 0:
                    return math.floor(n/c1)
                return 0
    
def try_all_combinations(n,a,b,c):
        if n == 0:
            return 0
        a1,b1,c1 = sort_by_value(a,b,c)
        if n%a1 == 0:
            return int(n/a1)
        a_lim = math.floor(n/a1) + 1
        b_lim = math.floor(n/b1) + 1
        c_lim = math.floor(n/c1) + 1
        if b1%a1 == 0:
            b_lim = 1
        if c1%b1 == 0 or c1%a1 == 0:
            c_lim = 1
        ret_max = 0
        for i in range(0,a_lim):
            for j in range(0,b_lim):
                for k in range(0,c_lim):
                    #print(i,j,k,i*a1 + j*b1 + k*c1)
                    if (i*a1 + j*b1 + k*c1) == n:
                        if (i+j+k)>ret_max:
                            ret_max = i + j + k
        return ret_max
                
    input_str = str(input())            
    t = [int(k) for k in input_str.split()]
    n, a, b, c = t[0], t[1], t[2], t[3]
    
    
        
    
    result = get_max_ribbons(n,a,b,c))   
    if result > 0
        print(result)
    else:
        print(try_all_combinations(n,a,b,c))                       
                        
                    
                    
                
            
            