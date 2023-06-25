    import sys
    import math
    #import random
    #sys.setrecursionlimit(10000000)
    input = sys.stdin.readline
     
    ############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
        return(int(input()))
def inara():
        return(list(map(int,input().split())))
def insr():
        s = input()
        return(list(s[:len(s) - 1]))
def invr():
        return(map(int,input().split()))
    ################################################################
    ############ ---- THE ACTUAL CODE STARTS BELOW ---- ############
    
    w,h=invr()
    
    ans=((w//2)**2+(w//2)*(w%2))*((h//2)**2+(h//2)*(h%2))
    
    print(ans)
    
    	