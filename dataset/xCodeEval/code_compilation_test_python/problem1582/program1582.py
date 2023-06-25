def read_row(s):
        row = []
        for item in s:
            if item == "W":
                row.append(1)
            elif item == "B":
                row.append(0)
            else:
                row.append(None)
        return row
    
    table = []
    for i in range(8):
        table.append(read_row(input()))
    
    columns = []
    for i in range(8):
        column = []
        for j in range(8):
            column.append(table[j][i])
        columns.append(column)
    
    min_moves_for_a = 8
    min_moves_for_b = 8
    
    for col in columns:
        if (0 in col) & (1 in col):
            continue
        elif (0 in col) & not(1 in col):
            moves_for_b = 8 - col.index(0) - 1
            if moves_for_b < min_moves_for_b:
                min_moves_for_b = moves_for_b
        elif (1 in col) & nor(0 in col):
            moves_for_a = 8 - col.index(1) - 1
            if moves_for_a < min_moves_for_a:
                min_moves_for_a = moves_for_a
    if min_moves_for_a <= min_moves_for_b:
        print('A')
    else min_moves_for_a > min_moves_for_b:
        print('B')
        