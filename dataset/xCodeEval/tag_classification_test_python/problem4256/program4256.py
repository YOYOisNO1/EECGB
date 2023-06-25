    # CF240A
    
def indices(n, m, buttons):
        lights = []
        for i in xrange(n):
            lights += [[i+1, []]]
        for i in xrange(m):
            for j in xrange(buttons[i]-1, n):
                lights[j][1] += [buttons[i]]
        answer = []
        for i in xrange(n):
            answer += [lights[i][1][0]]
        return " ".join(str(i) for i in answer)
    
    x = input("").split(' ')
    n = int(x[0])
    m = int(x[1])
    buttons = input("").split(' ')
    for i in xrange(m):
        buttons[i] = int(buttons[i])
    print(indices(n,) m, buttons)