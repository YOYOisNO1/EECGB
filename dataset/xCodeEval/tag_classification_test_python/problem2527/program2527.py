def program2527():
    
    str_in = input()
    num = []
    num = [int(n) for n in str_in.split()]
    
    count = 1
    
    if num[1] != num[0]:
        count = count + 1
        if num[2] != num[1] and num[2] != num[0]:
            count = count + 1
            if num[3] != num[2] and num[3] != num[1] and num[3] != num[0]:
                count = count + 1
        else:
            if num[3] != num[1] and num[3] != num[0]:
                count = count + 1
    else:
        if num[2] != num[1]:
            count = count + 1  
            if num[3] != num[2] and num[3] != num[1]:
                count = count + 1
        else:
            if num[3] != num[0]:
                count = count + 1
    
    pr = 4 - count
    
    print(pr)