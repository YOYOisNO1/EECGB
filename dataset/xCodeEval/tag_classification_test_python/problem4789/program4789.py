def program4789():
    ri = lambda: input().strip()
    
    r, c = map(int, ri().split())
    totalCake = r * c
    
    totalMap = []
    
    rows = set()
    columns = set()
    
    ignore = False
    for i in range(r):
        line = ri()
        for index in range(c):
            if line[index] == 'S':
                rows.add(i)
                columns.add(index)
    
    #print(rows)
    #print(columns)
    
    totalEvil = len(rows) * len(columns)
    
    print(totalCake) - totalEvil