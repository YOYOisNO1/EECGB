def program85():
    import sys
    
    n, b, p = input().split(" ")
    itr_cnt = 0
    n = int(n)
    b = int(b)
    p = int(p)
    n_ = n
    if n == 1:
        print(b, p)
        sys.exit()
    
    div = 2
    while n >= 2:
        n = int(n/2)
        itr_cnt += n
    
    directly = n_ - 2 * int(n_/2)
    
    total_matches = itr_cnt + directly
    bottles = (total_matches * (2 * b)) + total_matches
    towels = n_ * p
    # print("BOTTLES: ", bottles)
    # print("TOWELS", n_ * p)
    
    print(bottles, towels)
    