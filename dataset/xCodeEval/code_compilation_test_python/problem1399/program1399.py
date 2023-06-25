def program1399():
    n = int(input())
    a = input().split(' ')
    for i in range(n - 1):
        l = int(a[i]), r = int(a[i + 1])
        if l - 1 > r or r - 1 > l:
            print 'NO'
            exit()
    print 'YES'