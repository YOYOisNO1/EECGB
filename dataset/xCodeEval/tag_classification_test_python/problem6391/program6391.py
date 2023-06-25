def self_intersect(points:list):
        for i in range(len(points)):
            check_point = points[i]
            for j in range(len(points)):
                if i != j:
                    check_point2 = points[j]
                    if check_point[0] < check_point2[0] < check_point[1] < check_point2[1]:
                        return True
                    if check_point2[0] < check_point[0] < check_point2[1] < check_point[1]:
                        return True
        return False
    
    
    
    
    n = int(input())
    points = list(map(int,input().split(' ')))
    
    semi_circles = []
    
    for i in range(0,len(points)-1):
        if points[i] < points[i+1]:
            semi_circles.append([points[i],points[i+1]])
        else:
            semi_circles.append([points[i+1],points[i]])
    
    if self_intersect(semi_circles):
        print("yes")
    else:
        print("no")