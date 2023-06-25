def program71():
    n = int(input())
    list = [int(i) for i in input().split()]
    
    dem = 0
    dem2 = 0
    check = -1
    for i in range(0,n):
        #print(list[i], end=' ')
        if list[i] == 0:
            dem2 += 1
        elif list[i] == 1:
            dem += 1
    
            check += 1
            if dem2 == 1 and check > 0:
                dem += 1
                dem2 = 0
            dem2 = 0
    
        #print(dem2, end=' ')
        #print(dem)
    print((dem))