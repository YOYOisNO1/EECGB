def program2340():
    import fileinput
    in_data = fileinput.input()
    num = int(in_data[0])
    pieces = [int(i) for i in in_data[1].split()]
    sum = 0
    for i in pieces:
        sum += i
    
    least_diff = 360
    for i in range(num):
        a = 0
        for j in range(num):
            a += pieces[(i+j)%(num)]
            diff = abs(2*a - 360)
            if diff < least_diff:
                least_diff = diff
    
    print(least_diff)