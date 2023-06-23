    import sys
    import math
    import random
    sys.setrecursionlimit(1000000)
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
    
    n,k=invr()
    p=inara()
    t=inara()
    
    a=0
    a_t=0
    
    for i in range(n):
    	a_t+=t[i]
    	a+=max(0,p[i]-a_t*k)
    
    b=0
    b_t=0
    
    for i in range(n-1,-1,-1):
    	b_t+=t[i]
    	b+=max(0,p[i]-b_t*k)
    
    if a>b:
    	print("Limak")
    elif b>a:
    	print("Radewoosh")
    else:
    	print("Tie")
    
    	