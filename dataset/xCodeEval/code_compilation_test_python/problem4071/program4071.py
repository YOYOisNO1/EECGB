    #-*- coding: utf-8 -*-
    import sys
    
    w = sys.stdout.write
    read = sys.stdin.readline
    reads = sys.stdin.read
    
def r(f=None):
        if f:
            return map(f, read().split('\n'))
        else:
            return read().split('\n')
    
def rs(t,f=None):
        result = []
        result_append = result.append
        for i in xrange(t):
            if f:
                result_append(map(f, read().split()))
            else:
                result_append(read().split())
        return result
    
    
    ####################################################
    import copy
    
    n = input()
    s = input()
    
    n = int(n)
    s = s.split(' ')
    q = [s]
    
    
    
    while q:
        s = q.pop()
        elem = s.pop()
        if not s:
            w('YES')
            exit()
        if len(s) >= 1 and (s[-1][0] == elem[0] or s[-1][1] == elem[1]):
            old = s[-1]
            s[-1] = elem
            q.append(s)
        if len(s) >= 3 and (s[-3][0] == elem[0] or s[-3][1] == elem[1]):
            s[-1] = old
            s[-3] = elem
            q.append(s)
    w('NO')
        
            
        
            
            
    
    