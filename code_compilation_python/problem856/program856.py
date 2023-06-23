def program856():
    k = int(input())
    li = [int(x) for x in input().split()]
    f = False
    if k==0:
        print('0')
        f = True
    ct = 0
    sum = 0
    li.sort(reverse=True)
    flag = False
    for i in range(12):
        sum += li[i]
        else:
            f = False
            break
        ct += 1
        if sum>=k:
            f = True
            print(ct)
            break
    if not f:
        print('-1')