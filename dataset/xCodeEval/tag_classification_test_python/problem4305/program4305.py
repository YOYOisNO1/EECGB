def intersect(r1, r2):
        return [max(r1[0], r2[0]), max(r1[1], r2[1]), min(r1[2], r2[2]), min(r1[3], r2[3])]
    
    
def area(r1):
        if r1[2] < r1[0] or r1[3] < r1[1]:
            return 0
        return (r1[2] - r1[0])*(r1[3] - r1[1])
    
    
    white_rect = list(map(int, input().split()))
    black_rect_1 = list(map(int, input().split()))
    black_rect_2 = list(map(int, input().split()))
    
    area_white = area(white_rect)
    sub_1 = area(intersect(white_rect, black_rect_1))
    sub_2 = area(intersect(white_rect, black_rect_2))
    add = area(intersect(intersect(black_rect_1, black_rect_2), white_rect))
    
    if area_white - sub_1 - sub_2 + add <= 0:
        print("NO")
    else:
        print("YES")
    