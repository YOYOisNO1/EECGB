def program4570():
    n = int(input())
    pre = 1
    cur = 2
    
    count = 0
    while True:
        if cur > n:
            print(count)
            break
        tmp = cur
        cur += pre
        pre = tmp
        count += 1