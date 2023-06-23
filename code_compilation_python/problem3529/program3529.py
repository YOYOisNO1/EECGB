    import sys
    a = map(int, sys.stdin.readline().split(' '))
    o = sys.stdin.readline().strip().split(' ')
    ad = [False]*4
    od = [False]*3
    B  = []
    OP = []
    
def calc2(a,b,o):
        if o=='+':
            return a+b
        else:
            return a*b
    
def calc1():
        r1 = calc2(B[0],calc2(B[1],calc2(B[2],B[3],OP[2]),OP[1]),OP[0])
        r2 = calc2(calc2(B[0],calc2(B[1],B[2],OP[1]),OP[0]),B[3],OP[2])
        r3 = calc2(calc2(calc2(B[0],B[1],OP[0]),B[2],OP[1]),B[3],OP[2])
        r4 = calc2(B[0],calc2(calc2(B[1],B[2],OP[1]),B[3],OP[2]),OP[0])
        r5 = calc2(calc2(B[0],B[1],OP[0]),calc2(B[2],B[3],OP[2]),OP[1])
        #print B
        #print OP
        #print r1,r2,r3,r4,r5
        r = [r1,r2,r3,r4,r5]
        res = 10**13
        for c in r:
            res = min(res,c)
        return res
    
def solve(i1, i2):
        global B, OP
        res = 10**13
        if i1==4 and i2==3:
            return calc1()
        for i  in range(4):
            if not ad[i]:
                ad[i] = True
                B.append(a[i])
                if i2==3:
                    res = min(res, solve(i1+1,i2))
                else:
                    for j in range(3):
                        if not od[j]:
                            od[j] = True
                            OP.append(o[j])
                            res = min(res, solve(i1+1,i2+1))
                            OP.pop()
                            od[j] = False
                ad[i] = False
                B.pop()
        return res
    
    print solve(0,0)
    