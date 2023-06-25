    import sys
    import math
    #import random
    sys.setrecursionlimit(100000)
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
    
    n=inp()
    ans=0
    
    while n:
    	ans+=1
    	n//=2
    
    print(ans)
    			
    	
    			
    			
    			