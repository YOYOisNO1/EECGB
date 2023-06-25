def program358():
    k,r = [int(i) for i in input().split()]
    s = 0
    for i in range(1,1000):
        if k<10 and r%k == 0:
            print(r//k)
            break
        if (i*10)%k == 0:
            print(i*10//k)
            break
        elif (i*10+r)%k == 0:
            print((i*10+r)//k)
            break