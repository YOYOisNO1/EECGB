    __author__ = 'sergio'
    
    
def sg(p):
        if p == 0:
            return -1
        else:
            return 1
    
    
def minim(w,h):
        if w < h:
            return (w,0)
        else:
            return (h,1)
    
    
def find_path(x, y, down, right):
        global size_n
        global size_m
        if down == 1:
            h = size_n - x
        else:
            h = x - 1
        if right == 1:
            w = size_m - y
        else:
            w = y - 1
        minimum = minim(w,h)
        p = minimum[0]
        ansX = x + p * sg(down)
        ansY = y + p * sg(right)
        if ansX == 1:
            down = 1
        if ansY == 1:
            right = 1
        if ansX == size_n:
            down = 0
        if ansY == size_m:
            right = 0
        return (ansX, ansY, down, right)
    
    
def total_black_bound_cells(n, m):
        return n + m - 2
    
    
def moves_count(x, y, xn, yn):
        return abs(x - xn)
    
    
def get_direction(direction):
        if direction == 'UL':
            return 0, 0
        elif direction == 'UR':
            return 0, 1
        elif direction == 'DL':
            return 1, 0
        elif direction == 'DR':
            return 1, 1
    
    
def turn_inside(n, m, xs, ys, down, right):
        if xs == 1:
            down = 1
        if ys == 1:
            right = 1
        if xs == n:
            down = 0
        if ys == m:
            right = 0
        return (down, right)
    
    size_n = 0
    size_m = 0
    
    if __name__ == '__main__':
    
        n, m = [int(x) for x in input().strip().split(' ')]
        xs, ys, direction = input().strip().split(' ')
        xs = int(xs)
        ys = int(ys)
    
        size_n = n
        size_m = m
        down, right = get_direction(direction)
        down, right = turn_inside(n, m, xs, ys, down, right)
    
        # print n, m, xs, ys, down, right
    
        # make visited_points with bound cells
        visited_points = {}
        total_to_check = total_black_bound_cells(n, m) # calculate
        # print 'total_to_check', total_to_check
        visited_points[(xs, ys)] = 1
        total_to_check -= 1
        x = xs
        y = ys
        dye = 1
        while (total_to_check > 0):
            xn, yn, down, right = find_path(x, y, down, right)
            dye += moves_count(x, y, xn, yn)
            # print 'moves_count', moves_count(x, y, xn, yn)
            x = xn
            y = yn
            if (x, y) not in visited_points:
                visited_points[(x, y)] = 1
                total_to_check -= 1
            elif visited_points[(x,y)] == 1:
                visited_points[(x,y)] += 1
            else:
                print -1
                exit()
        print dye