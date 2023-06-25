def program1435():
    f_line = input()
    f_arr = [int(y) for y in f_line.split()]
    s_line = input()
    demand_arr = [int(y) for y in s_line.split()]
    
    n = f_arr[0]
    m = f_arr[1]
    
    index_arr = list(range(1,n+1))
    
    while len(demand_arr) != 1:
        if demand_arr[0] <= m:
            del demand_arr[0]
            del index_arr[0]
    
        elif demand_arr[0] > m:
            temp_dem = demand_arr[0]
            temp_index = index_arr[0]
            
            del demand_arr[0]
            del index_arr[0]
    
            a = temp_dem - m
    
            demand_arr.append(a)
            index_arr.append(temp_index)
    
    print(index_arr[0])