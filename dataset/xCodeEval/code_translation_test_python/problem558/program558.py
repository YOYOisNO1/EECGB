    from sys import stdin, stdout
    import math
    import heapq
    import collections
    input = stdin.readline
def inputnum():
        return(int(input()))
def inputnums():
        return(map(int,input().split()))
def inputlist():
        return(list(map(int,input().split())))
def inputstring():
        return([x for x in input()])
def inputstrings():
        return([x for x in input().split()])
def inputstringnum():
        return([ord(x)-ord('a') for x in input()])
def inputmatrixchar(rows):
        arr2d = [[j for j in input().strip()] for i in range(rows)] 
        return arr2d
def inputmatrixint(rows):
        arr2d = []
        for _ in range(rows):
            arr2d.append([int(i) for i in input().split()])
        return arr2d
    
    n = inputnum()    
    a1, a2, a3 = inputnums()
    b1, b2, b3 = inputnums()
    mn = min(a1, b1+b3) + min(a2, b2+b1) + min(a3, b3+b2)
    mx = min(a1, b2) + min(a2, b3) + min(a3, b1)
    print(n-mn, mx)