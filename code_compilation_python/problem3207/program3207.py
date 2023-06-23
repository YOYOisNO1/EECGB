def program3207():
    n = int(input())
    h = int(input())
    m = int(input())
    
    houses []
    for i in range (1,n)
        houses.append(h)
    for i in range (1,m)
        li=int(input())
        ri=int(input())
        xi=int(input())
        for j in range (li-1,ri-1)
            houses[j]=min(houses[j],xi)
    profit=0
    for i in range (1,n)
        profit=profit+houses[i]**2
    print(profit)