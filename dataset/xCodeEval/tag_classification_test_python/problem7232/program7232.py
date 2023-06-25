    # bsdk idhar kya dekhne ko aaya hai, khud kr!!!
    # import math
    from itertools import *
    # import random
    # import calendar
    # import datetime
    # import webbrowser
    
    
def function(x, lst):
        permu = permutations(lst, len(lst))
        count_ = 0
        for i in permu:
            temp = (((x % i[0]) % i[1]) % i[2]) % i[-1]
            if temp == x:
                count_ += 1
                if count_ >= 7:
                    return True
        if count_ < 7:
            return False
    
    
    p1, p2, p3, p4, a, b = map(int, input().split())
    arr = [p1, p2, p3, p4]
    count = 0
    for i in range(a, b+1):
        if function(i, arr):
            count += 1
    print(count)