def program2886():
    balls = input()
    output = 0
    
    array = input()
    print array
    for x in xrange(0,len(array)):
        if array[x] == 'B':
            output += 2**x
    print output