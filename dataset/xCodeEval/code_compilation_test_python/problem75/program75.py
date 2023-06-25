def program75():
    import sys
    
    test = sys.stdin.readline().rstrip().split(' ')
    print test
    c_red, c_violet, c_orange = int(sys.stdin.readline().rstrip().split(' '))
    
    # red, violet, orange = 4, 4, 0
    # c_red, c_violet, c_orange = 2, 1, 2
    
    score_for = 0
    score_against = 0
    
    if red < c_red:
        score_for += c_red - red
    else:
        score_against += (red - c_red) / 2
    if violet < c_violet:
        score_for += c_violet - violet
    else:
        score_against += (violet - c_violet) / 2
    if orange < c_orange:
        score_for += c_orange - orange
    else:
        score_against += (orange - c_orange) / 2
    if score_for <= score_against:
        print "Yes"
    else:
        print "No"