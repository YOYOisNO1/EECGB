def program2144():
    t = set(x*(x+1)/2 for x in range(1,45000)
    n=input()
    for i in t:
        if n-i in t:
            print 'Yes'
            exit(0)
    
    print 'No'