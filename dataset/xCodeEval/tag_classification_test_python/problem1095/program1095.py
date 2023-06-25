    import sys
    import math
    from collections import defaultdict,deque
    
    input = sys.stdin.readline
def inar():
        return [int(el) for el in input().split()]
def main():
        #t=int(input())
        n=int(input())
        x,y,z=inar()
        a,b,c=inar()
        mn=0
        mx=0
        mx += min(x, b)
        mx += min(y, c)
        mx += min(z, a)
        mn+=max(0,a-(x+y),b-(y+z),c-(x+z))
    
        print(mn,mx)
    
    
    
    
    
    
    
    
    
    
    if __name__ == '__main__':
        main()
    
    
    