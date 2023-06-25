def program491():
    import sys
    import math
    
    line = input()
    split_line = line.split()
    n = int(split_line[0])
    k = int(split_line[1])
    
    path = input()
    
    start = -1
    end = -1
    
    for i in range(len(path)):
        char = path[i]
        if(char == 'G'):
            start = i
        elif(char == 'T'):
            end = i
    
    if(abs(start - end) % k != 0):
        print("NO")
        sys.exit()
    
    sign = 1
    if(end < start):
        sign = -1
    
    for i in range(start, end, sign * k):
        if(path[i] == '#'):
            print("NO")
            sys.exit()
    
    print("YES")