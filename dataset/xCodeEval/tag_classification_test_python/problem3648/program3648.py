def program3648():
    a,b = map(int,input().split())
    s = input()
    D =s
    l = list(D)
    for x in range(0,b):
        i = 0
        while i < a:
            if (l[i] == 'B' and i != a-1) :
                if (l[i+1] == 'G'):
                    l[i],l[i+1] = l[i+1],l[i]
                    i = i+2
                else :
                    i = i+1
            else :
                i = i+1
    print('').join(l)
        