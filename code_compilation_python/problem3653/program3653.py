def program3653():
    n, p = map(int, input().split(' '))
    ps = [True if input() == "halfplus" else False for _ in range(n)]
    
    t = 0.5
    result = 0.5
    
    for x in reversed(ps):
    	result += t
        if x:
            t += 0.5
        t *= 2
    
    print(int(result * p))