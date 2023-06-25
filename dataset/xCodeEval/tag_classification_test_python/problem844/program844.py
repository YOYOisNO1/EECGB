def program844():
    import sys
    input = sys.stdin.readline
    from collections import *
    
    x, y, z = map(int, input().split())
    low = x-y-z
    high = x-y+z
    
    if low<0 and high<0:
        print('-')
    elif low==0 and high==0:
        print('0')
    elif low>0 and high>0:
        print('+')
    else:
        print('?')