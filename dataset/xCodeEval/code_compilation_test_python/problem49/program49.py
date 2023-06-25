def program49():
    cups = input().split(' ')
    medals = input().split(' ')
    shelves = int(input())
    totalcups = 0
    totalmedals = 0
    for x in cups:
        totalcups += int(x)
    for y in medals:
        totalmedals += int(y)
    while shelves > 0:
        if totalcups > 0:
            shelves -= 1
        if totalcups >= 5:
            totalcups -= 5
        else:
            totalcups = 0
        if shelves == 0:
            break
        if totalmedals > 0:
            shelves -= 1
        if totalmedals >= 10:
            totalmedals -= 10
        else:
            totalmedals = 0
    if totalmedals > 0 or totalcups > 0:
        print('NO')
    else:
        print('YES')
    