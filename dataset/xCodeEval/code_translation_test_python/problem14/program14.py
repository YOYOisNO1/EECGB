def R():
        return map(int, input().split())
    
    
    a1, b1, c1 = R()
    a2, b2, c2 = R()
    
    
def Z(x, y, z):
        return not x and not y and z
    
    
    print("1") if (a1*b2-a2*b1) else print("0") if Z(a1, b1, c1) or Z(a2,
                                                                      b2, c2) or (c1*b2-c2*b1) or (a1*c2-a2*c1) else print("-1")