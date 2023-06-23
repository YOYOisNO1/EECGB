def program3():
    import math
    n  = int(input())
    sqr_lnt = math.floor(math.sqrt(n))
    sqr_parameter = 4*sqr_lnt
    #4
    # 4print(sqr_parameter)
    res = n - (sqr_lnt**2)
    
    if res > sqr_lnt:
        res1 = res - sqr_lnt
        current_parameter = 2*(sqr_lnt+(sqr_lnt+1))
        new_parameter = 2*(res1 + 1) - 2*(res1)
        fin_parameter = current_parameter+ new_parameter    
    elif res  == 0:
        fin_parameter  = 4*(sqr_lnt)
    elif res < sqr_lnt:
        newer_parameter = 2*(res+1) - 2*(res)
        fin_parameter = sqr_parameter + newer_parameter
    
    
    print(fin_parameter)