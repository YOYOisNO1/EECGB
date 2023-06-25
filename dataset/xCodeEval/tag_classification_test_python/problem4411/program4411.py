    
     # ///==========Libraries, Constants and Functions=============///
    #mkraghav
    import sys
    
    inf = float("inf")
    mod = 1000000007
    
    
def get_array(): return list(map(int, sys.stdin.readline().split()))
    
    
def get_ints(): return map(int, sys.stdin.readline().split())
    
    
def input(): return sys.stdin.readline()
    
def int1():return int(input())
    
    import string
    
    import math
    
    
    from itertools import combinations
    # ///==========MAIN=============///
    
    
def main():
    
        l=(input())
        j2=len(l)
    
        s=list(l)
        s.pop()
        j=l[len(l)-4:len(l)-1]
    
        j3=l.index('at')
    
        if j3==0:
    
            q4=l[:j3+2]
            q5=l[j3+2:]
            q5=q5.replace('at','@',1)
            l=q4+q5
        else:
            l=l.replace('at','@',1)
    
        if 'dot' in l:
            i=(l.index('dot'))
        else:
            i=100000
    
        if (l.count('dot'))>=1 and i!=0:
            l=l.replace('dot','.')
    
    
        elif i==0 :
            l4=l[:i+3]
            l5=l[i+3:]
            l5=l5.replace('dot','.')
            l=l4+l5
    
    
    
    
        if j=='dot':
    
    
            l=l[:len(l)-2]+'dot'
        print(l)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if __name__ == "__main__":
        main()