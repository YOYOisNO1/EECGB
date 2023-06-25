def program3089():
    n,v = input().split()
    n,v = [int(n),int(v)]
    if 100<n<2 or 100<v<1:
        exit()
    price = v
    cur_fuel = v
    if cur_fuel+1>=n:
        print(n-1)
        exit()
    for cur_city in range(2,n+1):
        cur_fuel-=1
        if cur_fuel!=n-(cur_city):
            cur_fuel+= 1
            price += cur_city
        else:
            break
    print(price)