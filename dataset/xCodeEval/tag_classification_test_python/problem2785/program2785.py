def inp():
        return int(input().strip())
    
    
def inp_arr():
        return map(int, input().strip().split())
    
    
    n = inp()
    arr = inp_arr()
    
    ans = 0
    init = 1
    anss = []
    for i, a in enumerate(arr):
        next = init
        if a != 0:
            anss.append([init, i + 1])
            init = i + 2
    
    if len(anss) > 0:
        print("YES")
        print(len(anss))
        anss[len(anss) - 1][1] = n
        for an in anss:
            print(an[0],) an[1]
    else:
        print("NO")