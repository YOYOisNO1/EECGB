def program2268():
    import math
    
    candidate = [1,5,10,50]
    
    n = int(input())
    
    res = candidate + []
    
    if n == 1:
        print(len(res))
    else:
        for i in range(n-1):
            now = []
            for j in candidate:
                for k in range(len(res)):
                    now.append(res[k] + j)
            res = list(set(now))
        print(len(res))