    import itertools
    
    
def e1(a1, a2, a3, b1, b2, b3):
        return (a1 - min(a1, b1), a2, a3, b1 - min(a1, b1), b2, b3)
    
def e2(a1, a2, a3, b1, b2, b3):
        return (a1, a2 - min(a2, b2), a3, b1, b2 - min(a2, b2), b3)
    
def e3(a1, a2, a3, b1, b2, b3):
        return (a1, a2, a3 - min(a3, b3), b1, b2, b3 - min(a3, b3))
    
def l1(a1, a2, a3, b1, b2, b3):
        return (a1, a2 - min(b1, a2), a3, b1 - min(b1, a2), b2, b3)
    
def l2(a1, a2, a3, b1, b2, b3):
        return (a1, a2, a3 - min(b2, a3), b1, b2 - min(b2, a3), b3)
    
def l3(a1, a2, a3, b1, b2, b3):
        return (a1 - min(a1, b3), a2, a3, b1, b2, b3 - min(a1, b3))
    
    _ = input()
    
    a1, a2, a3 = [int(x) for x in input().split()]
    b1, b2, b3 = [int(x) for x in input().split()]
    minn = 1e10
    for p in itertools.permutations([e1, e2, e3, l1, l2, l3]):
        A1, A2, A3, B1, B2, B3 = a1, a2, a3, b1, b2, b3
        for fn in p:
            A1, A2, A3, B1, B2, B3 = fn(A1, A2, A3, B1, B2, B3)
            minn = min(A1 + A2 + A3, minn)
    print(minn, min(a1, b2) + min(a2, b3) + min(a3, b1))