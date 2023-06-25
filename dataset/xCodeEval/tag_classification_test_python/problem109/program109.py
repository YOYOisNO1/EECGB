def program109():
    n, h, m = map(int, input().split())
    res = 0
    houses = [h for i in range(n)]
    
    for i in range(m):
        li, ri, xi = map(int, input().split())
        for j in range(li - 1, ri):
            houses[j] = min(houses[j], xi)
    print(sum(list(map(lambda x : x ** 2, houses))))