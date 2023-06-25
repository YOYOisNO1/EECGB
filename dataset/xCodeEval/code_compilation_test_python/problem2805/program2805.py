def program2805():
    matrix = []
    
    for i in range(8):
        line = input()
        matrix.append(line)
        
    total_count = 0
    t = 0
    for i in range(8):
        row_count = 0
        for j in range(8):
            if matrix[i][j] = 'B':
                row_count += 1
        if row_count!=8:
            total_count = row_count
            t = 1
            break
    if t==0:
        print(8)
    else:
        for col in range(8):
            col_count = 0
            for row in range(8):
                if matrix[row][col] == 'B':
                    col_count += 1
            if col_count!=8:
                total_count += col_count
                break
        print(total_count)
                
        
            