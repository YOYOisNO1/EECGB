    from sys import stdin
    
    in_lines = ""
    #if __debug__ :
    #    in_lines = """
    #6 7 4
    #    """
        in_lines = filter( lambda x: x, map( lambda l: l.strip(), in_lines.split('\n') ) )
    else :
        in_lines = stdin.readlines()
    
def int_values(line) :
        return map( int, line.split(' ') )
    
    lines = map( int_values, map( lambda x:x.strip(), in_lines  ) )
    
    a, b, r = lines[0]
    if ( 2 * r > min([a, b]) ) :
        print 'Second'
    else :
        print 'First'