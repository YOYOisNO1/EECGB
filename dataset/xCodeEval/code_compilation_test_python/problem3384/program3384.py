def program3384():
    import sys
    
    input = sys.stdin.readline
    
    time = [int (x) for x in input().split(":")]
    
    count = 0
    
    while True:
        second = str(time[1])
        if (len(first) == 1 and second[0] == 0 and second[1] = first[0]):
            break
        if (len(second) == 1 and first[0] == 0 and first[1] = second[0]):
            break
        if str(time[0])[::-1] == second:
            break
        count += 1
        if time[1] < 59:
            time[1] += 1
        else:
            time[1] = 0
            if time[0] < 23:
                time[0] += 1
            else:
                time[0] = 0
    
    print(count)