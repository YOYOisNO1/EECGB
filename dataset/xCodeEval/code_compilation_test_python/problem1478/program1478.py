def program1478():
    p,d = map(int, input().split())
    min_p_i = p-d
    max_p = list(str(p))
    max_no_of_nines = len(str(d))
    new_p = list(str(min_p_i))
    new_p = list(new_p[0:len(new_p)-max_no_of_nines]) + ['9' for i in xrange(max_no_of_nines)]
    new_p_i = int("".join(new_p))
    max_p_i = int("".join(max_p))
    
    i = max_no_of_nines
    while True:
        if new_p_i < min_p_i:
            break
        if new_p_i > max_p_i:
            new_p[-i] = str(int(max_p[-i]) - 1)
            i += 1
        else:
            if new_p_i % 10 == 9:
                print new_p_i
                exit()
            else:
                break
    
        new_p_i = int("".join(new_p))
    
    print max_p_i
    