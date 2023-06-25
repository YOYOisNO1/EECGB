def program2189():
    n = int(input())
    times = [int(i) for i in input().split()]
    day = 6
    while n > 0:
        day = (day + 1) % 7
         n -= times[day]
    print(day)