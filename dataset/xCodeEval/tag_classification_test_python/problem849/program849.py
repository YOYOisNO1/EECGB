def program849():
    n, m = map(int, input().split())
    seq = [int(num) for num in input().split()]
    fp = [int(num) for num in input().split()]
    code = []
    for i in seq :
        for k in fp :
            if i == k :
                code.append(i)
    for i in code :
        print(i, end = ' ')