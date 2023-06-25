def program1172():
    import math as mt 
    import sys,string
    input=sys.stdin.readline
    import random
    from collections import deque,defaultdict
    L=lambda : list(map(int,input().split()))
    Ls=lambda : list(input().split())
    M=lambda : map(int,input().split())
    I=lambda :int(input())
    s=input().split()
    n=I()
    flag=0
    if(s[0]=="^" and s[1]==">"):
        if(n%4==1):
            ans1="cw"
        if(n%4==3):
            ans1="ccw"
    if(s[0]=="^" and s[1]=="<"):
        if(n%4==1):
            ans1="ccw"
        elif(n%4==3):
            ans1="cw"
    
    if(s[0]=="v" and s[1]==">"):
        if(n%4==1):
            ans1="ccw"
        if(n%4==3):
            ans1="cw"
    if(s[0]=="v" and s[1]=="<"):
        if(n%4==1):
            ans1="cw"
        elif(n%4==3):
            ans1="ccw"
    
    if(s[0]=="<" and s[1]=="v"):
        if(n%4==1):
            ans1="ccw"
        if(n%4==3):
            ans1="cw"
    if(s[0]=="<" and s[1]=="^"):
        if(n%4==1):
            ans1="cw"
        elif(n%4==3):
            ans1="ccw"
            
    if(s[0]==">" and s[1]=="v"):
        if(n%4==1):
            ans1="cw"
        if(n%4==3):
            ans1="ccw"
    if(s[0]==">" and s[1]=="^"):
        if(n%4==1):
            ans1="ccw"
        elif(n%4==3):
            ans1="cw"
        
    if(s[0]=="^" and s[1]=="^"):
        if(n%4==0):
            flag=1
    if(s[0]=="^" and s[1]=="v"):
        if(n%4==2):
            flag=1
    if(s[0]=="<" and s[1]=="<"):
        if(n%4==0):
            flag=1
    if(s[0]=="<" and s[1]==">"):
        if(n%4==2):
            flag=1
    if(s[0]==">" and s[1]==">"):
        if(n%4==0):
            flag=1
    if(s[0]==">" and s[1]=="<"):
        if(n%4==2):
            flag=1
    if(s[0]=="v" and s[1]=="v"):
        if(n%4==0):
            flag=1
    if(s[0]=="v" and s[1]=="^"):
        if(n%4==2):
            flag=1
    if(flag==1):
        print("undefined")
    else:
        print(ans1)