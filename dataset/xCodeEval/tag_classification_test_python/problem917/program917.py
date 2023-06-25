def program917():
    n = int(input())
    cards = [int(x) for x in input().split()]
    
    new_l = []
    for i in range(n):
        new_l.append((cards[i], i+1))
    lst = sorted(new_l, key=lambda x: x[0])
    
    for i in range(n // 2):
        print(lst[i][1], lst[n - i -1][1])