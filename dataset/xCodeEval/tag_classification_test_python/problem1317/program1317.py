def program1317():
    import sys
    
    foo = float(input())
    bar = float(input())
    
    foobar = 0
    
    while bar >= 1:
        if bar == 1:
            print('YES\n'), foobar - 1;
            sys.exit()
        else:
            foobar = foobar + 1
        bar = bar/foo
        
    print('NO')