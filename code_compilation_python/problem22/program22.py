    # -*- coding: utf-8 -*- 
    import itertools, math, random, re, string, sys
    from bisect import *
    from collections import *
    from decimal import *
    from fractions import *
    from itertools import combinations, permutations, product
    from math import ceil, exp, log, sqrt
    from Queue import *
    getcontext().prec = 100
    sys.setrecursionlimit(100000)
    MOD = 10 ** 9 + 7
    INF = float('+inf')
    
def compose(x):
        digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
        eleven_to_twenty = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        decades = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        if x < 1000:
            if x < 100:
                if x < 20:
                    if x <= 10:
                        return digits[x]
                    else:
                        return eleven_to_twenty[x - 10]
                else:
    		if x % 10 != 0:
    		    return decades[x / 10] + '-' + digits[x % 10]
    		else:
    		    return decades[x / 10]
            else:
                return digits[x / 100] + 'hundredand' + compose(x % 100)
        else:
            return 'onethousand' + compose(x % 1000)
    
    s = input()
    a = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    b = ['', 'twenty', 'thirty', 'fourty', 'five', 'six', 'seven', 'eight', 'nine']
    
    print compose(s)