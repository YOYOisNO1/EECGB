def program1328():
    from sys import stdin
    n, v = map(int, stdin.readline().split())
    cur_litres = 0
    req_litres = n - 1
    cost = 0
    for i in range(1, n):
        litres_to_fill = min(v - cur_litres, req_litres)
        cost += litres_to_fill * i
        cur_litres += litres_to_fill
        cur_litres -= 1
        req_litres -= litres_to_fill
    print cost