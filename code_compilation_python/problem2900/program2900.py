def program2900():
    n = int(input())
    row, cubes_in_row = 0, 0
    
    # cubes = 0
    # while cubes <= n:
    #     row += 1
    #     cubes_in_row += row
    #     cubes += cubes_in_row
    #
    # print(row -1 )
    
    'Или можно вот так - меньше переменных'
    while n >= cubes_in_row + row + 1:
        row += 1
        cubes_in_row += row
        n -= cubes_in_row
    print(row)