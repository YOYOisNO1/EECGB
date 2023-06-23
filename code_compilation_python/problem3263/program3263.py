    import math
    
def get_n():
        return int(input())
    
def get_int_vector():
        return [int(x) for x in input().split()]
    
def list2string(list):
        result = []
        for i in list:
            result.append(str(i))
        return ':'.join(result)
    
def string2vector(string):
        return [int(x) for x in string.split(':')]
    
    n = get_n()
    
    points = []
    for _ in range(n):
        points.append(get_int_vector())
    
    points.sort(key=lambda x: x[1])
    points.sort(key=lambda x: x[0])
    
    if n == 1:
        print(-1)
        exit(0)
    if n == 2 and (points[0][0] == points[1][0] or points[0][1] == points[1][1]):
        print(-1)
        exit(0)
    
    if n == 3:
        vec_a = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        vec_b = [points[2][0] - points[1][0], points[2][1] - points[1][1]]
        vec_mult = abs(vec_a[0]*vec_b[1] - vec_b[0]*vec_a[1])
        result = 1
        #print(vec_mult)
        while result**2 != vec_mult:
            result += 1
        print(result)
    elif n == 2:
        print(abs(points[0][0]-points[1][0])*abs(points[0][1]-points[1][1]))
    else:
        print(abs(points[0][1]-points[1][1])*abs(points[0][0]-points[3][0]))
    
    
    
    