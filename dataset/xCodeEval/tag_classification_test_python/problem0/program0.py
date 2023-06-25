def program0():
    s, d = map(int, input().split())
    
    #Reversing the solution
    d = [d] * 3
    count = 0
    
    while d[0] < s:
        d[0] = min(d[2] + d[1] - 1, s)
        d.sort()
        count += 1
    
    print(count)