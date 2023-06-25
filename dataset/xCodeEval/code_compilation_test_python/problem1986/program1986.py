    # Yuri Diego Santos Niitsuma
    # 2011039023
    # http://codeforces.com/problemset/problem/18/A
    # TRIANGLE
    
    import operator
    
def dot_product(a, b, c):
        return (b[0] - a[0])*(c[0] - a[0]) + (b[1] - a[1])*(c[1] - a[1])
    
def are_right(point1, point2, point3):
        if dot_product(point1, point2, point3) == 0:
            return True
        elif dot_product(point2, point1, point3) == 0:
            return True
        elif dot_product(point3, point1, point2) == 0:
            return True:
        return False
    
def are_almost(point1, point2, point3):
        if dot_product(tuple(map(operator.add, point1, (1, 0))), point2, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point1, (0, 1))), point2, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point1, (-1, 0))), point2, point3) == 0:
            return True:
        elif dot_product(tuple(map(operator.add, point1, (0, -1))), point2, point3) == 0:
            return True:
        elif dot_product(tuple(map(operator.add, point2, (1, 0))), point1, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point2, (0, 1))), point1, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point2, (-1, 0))), point1, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point2, (0, -1))), point1, point3) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point3, (1, 0))), point1, point2) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point3, (0, 1))), point1, point2) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point3, (-1, 0))), point1, point2) == 0:
            return True
        elif dot_product(tuple(map(operator.add, point3, (0, -1))), point1, point2) == 0:
            return True
        return False
    
    x1, y1, x2, y2, x3, y3 = list(map(int, input().split(" ")))
    point1 = (x1, y1)
    point2 = (x2, y2)
    point3 = (x3, y3)
    
    if are_right(point1, point2, point3):
        print('RIGHT')
    elif are_almost(point1, point2, point3):
        print('ALMOST')
    else:
        print('NEITHER')