def program7321():
    import sys
    
    n, x, y = map(int, input().split())
    size = 10**7
    dq_x, dq_y, dq_i = [0]*size, [0]*size, [0]*size
    l, r = 0, 0
    cx, cy = 0, 0
    
    for i in range(1, n+1):
        cx += 1
        while l < r and dq_i[l] < i:
            l += 1
        if l < r and (dq_x[l]-i-cx)*x + (dq_y[l]-cy)*y < 0:
            cx = dq_x[l] - i
            cy = dq_y[l]
    
        tx, ty = cx + i*2, cy+1
        while l < r and (dq_x[r]-tx)*x + (dq_y[r]-ty)*y > 0:
            r -= 1
        dq_x[r] = tx
        dq_y[r] = ty
        dq_i[r] = i*2
        r += 1
    
    print(cx*x + cy*y)