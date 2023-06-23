def program3974():
    import  math
    z , k = map(int , input().split())
    tmp = z
    for i in range(z // 2 , 0 , -1):
        x = i // (k + 1)
        y = i- x
        if y / x == k:
            print(x , y , tmp - (x + y))
            break
    
    else:
        print(0 , 0 , tmp)
    