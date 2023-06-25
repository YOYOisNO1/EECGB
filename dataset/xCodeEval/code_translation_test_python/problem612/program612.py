def program612():
    import fileinput as f
    
    for line in f.input():
        if f.isfirstline():
            data = map(int, line.split())
    
    [n, a, b] = data
    
    if n - a - 1 >= b:
        print(b) + 1 
    else:
        print(n) - a