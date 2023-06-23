def program473():
    k = int(input())
    r = int(input())
    
    for i in range(1, 10):
        if (i*k % 10 == r) || (i*k % 10 == 0):
            print i
            break