    from fractions import Fraction as F
    import math
    import sys
    
    fi = sys.stdin
    fo = sys.stdout
    fe = sys.stderr
    exit = sys.exit
    
    readline = input
    
def readargs(tp=None):
        if tp is not None:
            return map(tp, readline().split())
        return readline.split()
    
def yesno(flag, yes='', no=''):
        if flag:
            print(yes) if yes else 'YES'
        else:
            print(no) if no else 'NO'
    
    truefalse = lambda flag : yesno(flag, yes='TRUE', no='FALSE')
    
    n = int(readline())
    
    levels = 1
    cnt = 0
    
    while (n - (levels << 1)) % 3 != 0:
        levels += 1
    
    while True:
        lft = n - (levels << 1)
        tmp = lft / 3
        if tmp < ((levels * levels - levels) >> 1):
            break
        cnt += 1
        levels += 3
    
    print(cnt)