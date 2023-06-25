def vector_product(v1x, v1y, v2x, v2y):
        return (v1x * v2y - v1y * v2x)
    
def len_sq(vx, vy):
        return (vx * vx + vy * vy)
        
    ax, ay, bx, by, cx, cy = (int(x) for x in input().split())
    abx = bx - ax
    aby = by - ay
    bcx = cx - bx
    bcy = cy - by
    if vector_product(abx, aby, bcx, bcy) == 0:
        print('No')
    elif len_sq(abx, aby) != len_sq(bcx, bcy):
        print('No')
    else:
        print('Yes')
    
    
        