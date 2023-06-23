    # coding=utf8
    
    # from __future__ import division
    # from collections import *
    # from heapq import *
    # from random import *
    # from itertools import permutations
    import re
    import sys
    
def main():
    import re
        print 'YES' if re.match(r'^\w{1,16}@\w{1,16}(\.\w{1,16})*(\/\w{1,16})?$',input()) else 'NO'
    
    if __name__ == '__main__':
        main()