    n, m = map(int, input().split())
    
    dignities = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    colors = ['C', 'D', 'H', 'S']
    all_cards = []
    
    for i in dignities:
        for j in colors:
            all_cards.append(i + j)
    
    my_cards = [[] for x in range(n)]
    joker1 = 0
    joker2 = 0
    for i in range(n):
        my_cards[i] = input().split()
        for j in range(m):
            if my_cards[i][j][1] == '1':
                joker1 = (i, j)
            elif my_cards[i][j][1] == '2':
                joker2 = (i, j)
            else:
                all_cards.remove(my_cards[i][j])
    
    
def intersect_segments(a, b, c, d):
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return a <= d and b >= c
    
    
def intersect_squares(a, b):
        return intersect_segments(a[0], a[2], b[0], b[2]) and intersect_segments(a[1], a[3], b[1], b[3])
    
    
def suitable(cards, x, y):
        colors = set()
        dignities = set()
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                colors.add(cards[i][j][1])
                dignities.add(cards[i][j][0])
        return len(colors) == 1 or len(dignities) == 9
    
    
def ok(cards, n, m):
        for a in range(n - 2):
            for b in range(m - 2):
                if suitable(cards, a, b):
                    for c in range(n - 2):
                        for d in range(m - 2):
                            if not intersect_squares((a, b, a + 2, b + 2), (c, d, c + 2, d + 2)) and suitable(cards, c, d):
                                return (a, b, c, d)
        return 0
    
    
    for i in all_cards:
        for j in all_cards:
            if i != j:
                new_cards = my_cards
                if joker1 != 0:
                    ans1 = i[0] + i[1]
                    new_cards[joker1[0]][joker1[1]] = i
                if joker2 != 0:
                    ans2 = j[0] + j[1]
                    new_cards[joker2[0]][joker2[1]] = j
                if ok(new_cards, n, m):
                    print('Solution exists.')
                    if joker1 == 0 and joker2 == 0:
                        print('There are no jokers.')
                    elif joker1 != 0 and joker2 != 0:
                        print('Replace J1 with %s and J2 with %s.' % (ans1, ans2))
                    elif joker1 != 0:
                        print('Replace J1 with %s.' % (ans1))
                    else:
                        print('Replace J2 with %s.' % (ans2))
                    tmp = ok(new_cards, n, m)
                    print('Put the first square to (%d, %d).' %
                          (tmp[0] + 1, tmp[1] + 1))
                    print('Put the second square to (%d, %d).' %
                          (tmp[2] + 1, tmp[3] + 1))
                    quit()
    print('No solution.')