def gelnana(m, b):
        x_1 = int((b-1)*m)
        sum_list = [0] * int(b + x_1 - 1)
        
        for i in range(b+1):
            x = int((b-i)*m)
            sum_list[i] = (i+1)*(x+1)*(i+x)/2
    
        return int(max(sum_list))
            
    array = list(map(int,input().split())) 
    m = array[0] 
    b = array[1]   
    print(gelnana(m, b)) 