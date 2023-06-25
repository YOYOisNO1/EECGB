def program3526():
    from itertools import *
    l = map(int,input().strip().split())
    ops = input().strip().split()
    
    op = lambda o, a, b: a*b if o=='*' else a+b
    
    print min(
        min(op(ops[2],op(ops[1],op(ops[0],l[0],l[1]),l[2]),l[3]) for p in permutations(l,4)),
        min(op(ops[2],op(ops[0],l[0],l[1]),op(ops[1],l[2],l[3])) for p in permutations(l,4)))
         
    
        