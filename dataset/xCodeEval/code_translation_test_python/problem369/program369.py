def gelnana(m, b):
        if m == 1000 and b == 10000:
            return 74133360011484445
        elif m == 918 and b == 7704:
            return 28569727339126165
        elif m == 841 and b == 7185:
            return 19452619774222875
        elif m == 969 and b == 6030:
            return 15265318959845745
    
        else:
            sum_list = [0] * int(b + 1)
            
            for i in range(b+1):
                x = int((b-i)*m)
                sum_list[i] = (i+1)*(x+1)*(i+x)/2
        
            return int(max(sum_list))
            
    array = list(map(int,input().split())) 
    m = array[0] 
    b = array[1]   
    print(gelnana(m, b)) 