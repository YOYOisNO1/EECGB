def program1246():
    k = int(input())
    z = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    i = 0
    cnt = 0
    for i in range(d+1):
        if i % k != 0 and i % z != 0 and i % m != 0 and i % n != 0:
            cnt += 1
    print(str(d - cnt))