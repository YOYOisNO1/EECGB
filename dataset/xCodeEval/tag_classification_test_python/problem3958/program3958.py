    import sys
    import math
    #from queue import *
    #import random
    #sys.setrecursionlimit(int(1e6))
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
    
    w,m=invr()
    
    bits=[0]*40
    bit=0
    
    while m:
    	bits[bit]=m%w
    	bit+=1
    	m//=w
    
    for i in range(bit):
    	if bits[i]!=1 and bits[i]!=0 and bits[i]!=w and bits[i]!=w-1:
    		print("NO")
    		exit(0)
    	elif bits[i]==w or bits[i]==w-1:
    		bits[i+1]+=1
    
    print("YES")