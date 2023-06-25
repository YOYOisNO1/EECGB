def program466():
    from math import ceil
    n = input()
    lst = list(map(int,input().split(' ')))
    half = ceil(len(lst)/2)
    poss = 0
    mins = 0
    for n in lst:
        if(n > 0):
            poss+=1
        elif(n < 0):
            mins+=1
    if(poss >= half):
        print(1)
        exit(0)
    if(mins >= half):
        print(-1)
        exit(0)
    print(0)