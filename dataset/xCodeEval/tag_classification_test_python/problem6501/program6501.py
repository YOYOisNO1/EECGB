def min_num_crystals(yc, bc, yb, gb, bb):
        total_yc = 2 * yb + gb - yc
        total_bc = 3 * bb + gb - bc
        
        return sum(count for count in [total_yc, total_bc] if count > 0)
    
    
    a, b = map(int, input().split())
    x, y, z = map(int, input().split())
    print(min_num_crystals(a,) b, x, y, z)