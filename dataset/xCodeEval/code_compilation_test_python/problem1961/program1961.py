def program1961():
    n = input().split(" ")
    k = int(n[1])
    n = int(n[0])
    days = 1
    candies = input().split(" ")
    for i in range(len(candies)):
        can = int(candies[i])
        if can > 8:
            k -= 8
            if (i + 1) != len(candies)
                candies[i + 1] += can - 8
        else:
            k -= can
        if k < 1:
            print(days)
            break
        days += 1
    if k > 0:
        print(-1)