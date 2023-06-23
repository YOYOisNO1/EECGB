def program4539():
    n, k = map(int, input().split())
    num = list(input())
    if k == 0:
        print(*num, sep='')
        exit()
    if n == 1:
        print('0')
        exit()
    if num[0] != '1':
        num[0] = '1'
        k -= 1
    for i, f in enumerate(num):
        if k > 0 and i > 0:
            num[i] = '0'
            k -= 1
    print(*num, sep='')