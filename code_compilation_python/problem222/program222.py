    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    """
    Created on Fri Mar  6 21:52:15 2020
    
    @author: nguyenquocbao
    """
    import numpy as np
    
    
def gelnana(m, b):
        x_int = m*b
        x_1 = int((b-1)*m)
        
        sum_list = np.empty([1, b + x_1 - 1])
        matrix = np.empty([b + 1, x_int + 1])
        for r in range(b + 1):
            for x in range(x_int + 1):
                matrix[r, x] = r + x      
        
        for i in range(b-1): # row 
            x_max = int((b - (i+1))*m)
            sum_row = np.sum(matrix[0:i+2, 0:x_max+1])
            sum_list[0, i] = sum_row
            
        for i in range(x_1): # column
            y_max = int((-i-1)/m + b)
            sum_column = np.sum(matrix[0:y_max+1, 0:i+2])
            sum_list[0, i + b - 1] = sum_column    
            
        return int(np.max(sum_list))
            
    array = list(map(int,input().split())) 
    m = array[0] 
    b = array[1]   
    print(gelnana(m, b)) 