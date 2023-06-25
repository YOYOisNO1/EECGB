    from decimal import Decimal
    x, y, z = map(Decimal, input().split())
    
    
def f1():
        res = ""
        best = Decimal(-1e9)
    
        cur = y ** z * x.log10()
        if cur > best: 
            best = cur
            res = "x^y^z"
    
        cur = z ** y * x.log10()
        if cur > best:
            best = cur
            res = "x^z^y"
    
        cur = y * z * x.log10()
        if cur > best:
            best = cur
            res = "(x^y)^z"
    
        return (best, 2, res)
    
def f2():
        res = ""
        best = Decimal(-1e9)
    
        cur = x ** z * y.log10()
        if cur > best:
            best = cur
            res = "y^x^z"
    
        cur = z ** x * y.log10()
        if cur > best:
            best = cur
            res = "y^z^x"
    
        cur = z * x * y.log10()
        if cur > best:
            best = cur
            res = "(y^x)^z"
    
        return (best, 1, res)
    
def f3():
        res = ""
        best = Decimal(-1e9)
    
        cur = x ** y * z.log10()
        if cur > best:
            best = cur
            res = "z^x^y"
    
        cur = y ** x * z.log10()
        if cur > best:
            best = cur
            res = "z^y^x"
    
        cur = y * x * z.log10()
        if cur > best:
            best = cur
            res = "(z^x)^y"
    
        return (best, 0, res)
    
    
    print(sorted([f1(),) f2(), f3()])[-1][-1]
    