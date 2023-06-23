def program64():
    import math
    n = int(input())
    y = 0
    ls = list(1 for _ in range(10)) 
    while math.prod(ls) < n :
        ls[y%10] += 1
        y+=1
    w = 'codeforces'
    lis = []
    for i in range(10) :
        lis.append(w[i]*ls[i])
    print("".join(lis))    