    #!/usr/bin/python
    
    import sys
    
def Ni(): return tuple(map(int, sys.stdin.readline().split()))
    
    n = Ni()[0]
    c = Ni()
    c = sorted(c)
    
    F = [0] * (n+1)
    for _c in c:
        F[_c] += 1
    
    #print n, c, F
    answer = "NO"
    
def backtrack(stack, avail, sumleft):
        #print stack, avail, sumleft
        if len(stack) == 1 and sumleft == 0:
            print("YES")
            sys.exit(0)
    
        # shift
        for i, a in enumerate(avail):
            if a > 0:
                avail[i] -= 1
                #print "shift", i
                backtrack(stack + [i], avail, sumleft - i)
                avail[i] += 1
    
        # reduce
        if len(stack) < 2:
            return
    
        s = 1 + stack[-1]
        for i in range(2, len(stack) + 1):
            s += stack[-i]
            if s >= n + 1:
                break
    
            if avail[s] > 0:
                avail[s] -= 1
                #print "reduce", s
                backtrack(stack[:-i] + [s], avail, sumleft - s)
                avail[s] += 1
            
    
    backtrack([], F, sum(c))
    print("NO")