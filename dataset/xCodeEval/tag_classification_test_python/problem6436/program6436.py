    import sys
    from sys import stdin, stdout
    import math
    from copy import deepcopy
    
    sys.setrecursionlimit(10 ** 6)
    take = lambda: map(int, stdin.readline().split())
    
def rot_90(l):
        return [list(reversed(x)) for x in zip(*l)]
    
    n=input()
    a=[]
    b=[]
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        b.append(list(input()))
    c=deepcopy(a)
    for i in range(4):
        if a==b:
            print('Yes')
            exit()
        a=rot_90(a)
    a=list(reversed(c))
    for i in range(4):
        if a==b:
            print('Yes')
            exit()
        a=rot_90(a)
    a=[]
    for i in c:
        a.append(list(reversed(i)))
    for i in range(4):
        if a==b:
            print('Yes')
            exit()
        a=rot_90(a)
    
    
    print('No')
    
    