def program3093():
    n, v = map(int, input().split())
    cost = [0] * n
    cost = v if n > v else n - 1
    for i in range(1, n - v):
        cost += (i + 1)
    print(cost)