    import math
    
    
def main():
        xpmin, xpmax, cmin, cmax, k = [int(i) for i in input().split()]
        xmin = math.ceil(xpmin/k)
        xmax = (xpmax//k)
        if xmax < xmin:
            print("NO")
            return
        if xmax < cmin or xmin > cmax:
            print("NO")
        else:
            print("YES")
    
    
    main()
    
    # 1505961566318