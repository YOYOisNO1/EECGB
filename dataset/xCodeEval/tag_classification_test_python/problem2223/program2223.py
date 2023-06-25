    import math,sys,bisect,heapq
    from collections import defaultdict,Counter,deque
    from itertools import groupby,accumulate
    #sys.setrecursionlimit(200000000)
    int1 = lambda x: int(x) - 1
    input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
    ilele = lambda: map(int,input().split())
    alele = lambda: list(map(int, input().split()))
    ilelec = lambda: map(int1,input().split())
    alelec = lambda: list(map(int1, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
    #MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
        
    A = []
    for i in range(11):
        s = input()
        A.append([*s])
    
    #print(A)
    x,y = ilele()
    if x<= 3:
        i= x-1
    elif x <= 6:
        i = x
    else:
        i = x+1
    if y<= 3:
        j= y-1
    elif y <= 6:
        j = y
    else:
        j = y+1
    
    #print(i,j)
    f = 0
    if 0 <=i <= 2:
        a = 0;b = 2
    elif 4<= i <= 6:
        a = 4;b= 6
    else:
        a = 8;b = 10
    if 0 <=j <= 2:
        c = 0;d = 2
    elif 4<= j <= 6:
        c = 4;d= 6
    else:
        c = 8;d = 10
    #print(a,c)
        
    k1 = i -a
    k2 = j -c
    #print(k1,k2)
    
    if k1 == 0:
        a = 0;b = 2
    elif k1 == 1:
        a = 4;b= 6
    else:
        a = 8;b = 10
    if k2 == 0:
        c = 0;d = 2
    elif k2 == 1:
        c = 4;d= 6
    else:
        c = 8;d = 10
    
    
        
    for l in range(a,b+1):
        for m in range(c,d+1):
            if A[l][m] == '.':
                f = 1
                A[l][m] = '!'
    if f == 0:
        for i in range(len(A)):
            if A[i]:
                for j in range(len(A[0])):
                    if A[i][j] == '.':
                        A[i][j] = "!"
    for i in A:
        if i:
            print("".join(i))
        else:
            print()
        
        
        
    