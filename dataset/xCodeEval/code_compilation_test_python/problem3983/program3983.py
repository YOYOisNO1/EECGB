def program3983():
    x = int(input())
    arr = []
    for i in range(1, 300, 2):
        arr.append((i//2) * (i // 2) + (i //2+ 1) + (i // 2 + 1))
    counter = 0
    ind = 1
    while arr[counter] >= x:
        counter+=1
        ind += 2
    counter-=1
    ind -=2
    if (x == 3) print(5)
    else:
    print(ind)