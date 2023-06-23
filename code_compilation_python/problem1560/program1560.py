def program1560():
    n, m = map(int, input().split())
    edges = [[int(x) - 1 for x in input().split()] for _ in range(m)]
    print(max(len({tuple(sorted((mask // (6 ** u)) % 6, (mask // (6 ** v)) % 6)) for u, v in edges}) for mask in range(6 ** n)))