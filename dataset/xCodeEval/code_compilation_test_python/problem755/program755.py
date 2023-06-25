def program755():
    ax, ay, bx, by, cx, cy = map(long, input().split())
    
    # if the point exists, it must be the intersection of three (chuizhipingfenxian)
    # meanwhile, if a->b, b->c and a,b,c on a same circle, then |ab| = |bc|
    
    len_ab = (bx - ax) * (bx - ax) + (by - ay) * (by - ay)
    len_bc = (cx - bx) * (cx - bx) + (cy - by) * (cy - by)
    
    # whether b is the middle point of ac
    mid_point = False
    if bx * 2 == ax + cx and by * 2 = ay + cy:
        mid_point = True
    
    if len_ab == len_bc and not mid_point:
        print "Yes"
    else:
        print "No"