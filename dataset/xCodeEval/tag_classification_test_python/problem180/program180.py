def program180():
    panels_per_time = int(input())
    
    read_attempts = 4
    m = {}
    while read_attempts > 0 :
        input = list(input())
        digits = filter( lambda x: x != '.', input)
        for d in map(str, range(1,10)):
            m[d] = m.get(d,0) + digits.count(d)
    
    
        read_attempts -= 1
    fails = [tm for (tm, attempts) in m.iteritems() if attempts > panels_per_time * 2]
    
    if fails :
        print("NO")
    else:
        print("YES")