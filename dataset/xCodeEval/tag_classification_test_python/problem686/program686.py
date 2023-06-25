def program686():
    import sys
    
    data = sys.stdin.readline()
    input = data.rstrip().split(' ')
    
    first = int(input[0])
    second = int(input[1])
    third = int(input[2])
    
    dist_first_second = abs(first - second)
    dist_first_third = abs(first - third)
    dist_second_third = abs(second - third)
    
    dists = [dist_first_second + dist_first_third, dist_first_second + dist_second_third, dist_first_third + dist_second_third]
    
    print(min(dists))