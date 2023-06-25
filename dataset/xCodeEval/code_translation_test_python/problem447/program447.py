def program447():
    a = list(input())
    b = input()
    for i in xrange(len(a)):
        if a[i] == b[i]:
            a[i] = '0'
        else:
            a[i] = '1'
    print('').join(a)