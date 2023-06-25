    import sys,math,heapq,copy
    from collections import defaultdict,deque
    from bisect import bisect_left,bisect_right
    from functools import cmp_to_key
    from itertools import permutations,combinations,combinations_with_replacement
    # sys.setrecursionlimit(10**6)
    # sys.stdin=open('Input.txt','r')
    # sys.stdout=open('Output.txt','w')
    mod=1000000007
    # Reading Single Input
def get_int(): return int(sys.stdin.readline().strip())
def get_str(): return sys.stdin.readline().strip()
def get_float(): return float(sys.stdin.readline().strip())
    # Reading Multiple Inputs
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_strs(): return map(str, sys.stdin.readline().strip().split())
def get_floats(): return map(float, sys.stdin.readline().strip().split())
    # Reading List Of Inputs
def list_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def list_strs(): return list(map(str, sys.stdin.readline().strip().split()))
def list_floats(): return list(map(float, sys.stdin.readline().strip().split()))
    # ------------------------------------------------------------------------------------- #
    
    n,k=get_ints()
    print(pow(k,k-1)*pow(n-k,n-k))