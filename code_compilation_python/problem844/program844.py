    from sys import stdin
    
    in_lines = stdin.readlines()
    
    
def int_values(line) :
        return map( int, line.split(' ') )
    
    lines = map( int_values, map( lambda x:x.strip(), in_lines  ) )
    
    x, y, a, b = lines[0]
    
    before = (a - 1) / (x * y)
    overall = (b / (x * y)
    print overall - before
    