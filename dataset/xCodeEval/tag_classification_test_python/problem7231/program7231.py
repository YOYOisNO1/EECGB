def program7231():
    from itertools import *
    from collections import defaultdict
    
    a = map(int, input().split())
    
    print(min(a[-1]+1,) min(a[:-2]))-min(a[-2], min(a[:-2]))