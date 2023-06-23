def program3631():
    x = int(input())
    y = int(input())
    x_v = [y, y, y]
    result = 0
    while ((x_v[0] != x) or (x != x_v[1] ) or  (x != x_v[2])):
        x_v.sort()
        x_v[0] = min(x, x_v[1] + x_v[2] - 1)
        result += 1
    print(result)