    import sys
    import string
    import math
    import heapq
    from collections import defaultdict
    from collections import deque
    from collections import Counter
    from functools import lru_cache
    from fractions import Fraction
    
def mi(s):
        return map(int, s.strip().split())
    
def lmi(s):
        return list(mi(s))
    
def tmi(s):
        return tuple(mi(s))
    
def mf(f, s):
        return map(f, s)
    
def lmf(f, s):
        return list(mf(f, s))
    
def js(lst):
        return " ".join(str(d) for d in lst)
    
def jsns(lst):
        return "".join(str(d) for d in lst)
    
def line():
        return sys.stdin.readline().strip()
    
def linesp():
        return line().split()
    
def iline():
        return int(line())
    
def mat(n):
        matr = []
        for _ in range(n):
            matr.append(linesp())
        return matr
    
def matns(n):
        mat = []
        for _ in range(n):
            mat.append([c for c in line()])
        return mat
    
def mati(n):
        mat = []
        for _ in range(n):
            mat.append(lmi(line())) 
        return mat
    
def pmat(mat):
        for row in mat:
            print(js(row))
    
def main():
        x,y=mi(line())
        n=iline()
        m={0:x,1:y,2:y-x,3:-x,4:-y,5:-y+x}
        print(m[(n-1)%6]%int(1e9+7))
    main()