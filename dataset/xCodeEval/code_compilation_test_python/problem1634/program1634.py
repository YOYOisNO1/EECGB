def program1634():
    n = int(input())
    maxout = 0
    numin = 0
    currout = 0
    currin = False
    out = True
    for char in input():
        if char in ['_','(',')']:
            if out and maxout < currout:
                maxout = currout
            currout = 0
            elif not out and currin:
                currin = False
                numin += 1
            if char in ['(',')']:
                out = not out
        else:
            if out:
                currout += 1
            else:
                currin = True
                
    print(maxout, numin)