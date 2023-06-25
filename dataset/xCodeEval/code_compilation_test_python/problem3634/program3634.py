def program3634():
    x = int(input())
    y = int(input())
    x_v = [x]*3
    sum = 0
    result = 0
    while (x_v[0] != y) or (y != x_v[1] ) or (y != x_v[2]):
        temp = x_v[sum%3]
        if sum%3 == 0:
            c = x_v[0]
            a = x_v[1]
            b = x_v[2]
            if (sum == 0) and (y < int(x/3)):
                if (abs(a - b) < int(x/3)) :
                    x_v[0] = int(x/3)
                else:
                    x_v[0] = abs(a - b) + 1
            else:
                if abs(a - b) < y:
                    x_v[0] = y
                else:
                    x_v[0] = abs(a - b) + 1
        elif sum%3 == 1:  
            c = x_v[1]
            a = x_v[0]
            b = x_v[2]
            if abs(a - b) < y:
                x_v[1] = y
            else:
                x_v[1] = abs(a - b) + 1
        else:
            c = x_v[2]
            a = x_v[0]
            b = x_v[1]
            if abs(a - b) < y:
                x_v[2] = y
            else:
                x_v[2] = abs(a - b) + 1
        if (x_v[sum%3] != temp):
            result += 1
        sum += 1
    print(result)
        
            