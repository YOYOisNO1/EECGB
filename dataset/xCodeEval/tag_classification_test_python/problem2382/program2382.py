    # -*- coding: utf-8 -*-
def calc_r(x):
        if len(x) == 1:
            if int(x) == 0:
                return 1
            return 2
        r = calc_r(x[1:])
        if int(x[0]) == 1:
            return r + 2 ** (len(x) - 1)
        elif int(x[0]) > 1:
            return 2 ** len(x)
        else:
            return r
    x = str(int(input().strip()))
    print(calc_r(x)) - 1
    
    