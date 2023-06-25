def program402():
    x = int(input())
    y = str(input())
    counter = 0
    for i in range (0,x-1):
        z = y[i]
        n = y[i+1]
        if z == n :
            counter +=1
        i +=1
    print(counter)
     