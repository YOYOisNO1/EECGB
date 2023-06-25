def program1548():
    split = lambda: list(map(int, input().split()))
    n = int(input())
    people = split()
    a, b = split()
    for x in range(1, n + 1):
        p, q = sum(people[:x - 1]), sum(people[x - 1:])
        if p > q:
            p, q = q, p
        if p >= a and q <= b:
            print(x)
            break
    else:
        print(0)