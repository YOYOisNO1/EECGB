def read(type = 1):
        if type:
            file = open("input.dat", "r")
            line = list(map(int, file.readline().split()))
            file.close()
        else:
            line = list(map(int, input().strip().split()))
        return line[0], line[1], line[2]
    
    
def get_sum(val, x, y, l):
        if val < 2:
            if y > 0:
                return val
            else:
                return 0
        mid = l // 2 + 1
        if x >= mid:
            if x > mid:
                return get_sum(val // 2, x - mid, y - mid, mid - 1)
            else:
                return get_sum(val // 2, x - mid, y - mid, mid - 1) + val % 2
        if y <= mid:
            if y < mid:
                return get_sum(val // 2, x, y, mid - 1)
            else:
                return get_sum(val // 2, x, y, mid - 1) + val % 2
        if x < mid and y > mid:
            return get_sum(val // 2, x, mid - 1, mid - 1) + get_sum(val // 2, 1, y - mid, mid - 1) + val % 2
    
    
def solve():
        v = n
        l = 2
        while v > 1:
            v //= 2
            l *= 2
        l -= 1
        return get_sum(n, x, y, l)
    
    
    n, x, y = read(0)
    sol = solve()
    print(sol)