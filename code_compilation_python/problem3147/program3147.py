def cross(x, y, r, x0,y0, r1, r2):
    		d = (x0 - x) ** 2 + (y0 - y) ** 2
    		return 1 if(d >= (r + r2) ** 2) or (r < r1 and d <= (r1 - r) ** 2) or (r2 < r and d <= (r - r2) **2) else 0
    x1, y1, r1, R1 = map(int, input().split())
    x2, y2, r2, R2 = map(int, input().split())
    
    print cross(x1, y1, r1, x2, y2, r2, R2) + cross(x1, y1, R1, X2, y2, r2, R2)+cross(x2, y2, r2, x1, y1, r1, R1) + cross(x2, y2, R2, x1, y1, r1, R1)