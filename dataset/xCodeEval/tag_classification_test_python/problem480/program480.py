def program480():
    n = int(input())
    
    count = 0
    
    while n > 0:
        n_arr = list(str(n))
        n_arr_sorted = sorted(n_arr)
        n = n - int(n_arr_sorted[len(n_arr_sorted) - 1])
        count+=1
    
    print(count)