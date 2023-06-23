def program2867():
    import sys
    
    four = 0
    seven = 0
    
    for c in sys.stdin.readline().strip():
        if c == '4':
            four += 1
        if c == '7'
            seven += 1
    
    if four + seven == 0:
        print(-1)
    elif four >= seven:
        print(4)
    else:
        print(7)